'''
brozzler/worker.py - BrozzlerWorker brozzles pages from the frontier, meaning
it runs youtube-dl on them, browses them and runs behaviors if appropriate,
scopes and adds outlinks to the frontier

Copyright (C) 2014-2018 Internet Archive

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import logging
import brozzler
import brozzler.browser
import threading
import time
import youtube_dl
import urllib.request
import json
import PIL.Image
import io
import socket
import collections
import requests
import doublethink
import tempfile
import urlcanon
from requests.structures import CaseInsensitiveDict
import rethinkdb as r
import datetime
import urllib.parse

_orig_webpage_read_content = youtube_dl.extractor.generic.GenericIE._webpage_read_content
def _webpage_read_content(self, *args, **kwargs):
    content = _orig_webpage_read_content(self, *args, **kwargs)
    if len(content) > 20000000:
        logging.warn(
                'bypassing youtube-dl extraction because content is '
                'too large (%s characters)', len(content))
        return ''
    return content
youtube_dl.extractor.generic.GenericIE._webpage_read_content = _webpage_read_content

class ExtraHeaderAdder(urllib.request.BaseHandler):
    def __init__(self, extra_headers):
        self.extra_headers = extra_headers
        self.http_request = self._http_request
        self.https_request = self._http_request

    def _http_request(self, req):
        for h, v in self.extra_headers.items():
            if h.capitalize() not in req.headers:
                req.add_header(h, v)
        return req

class YoutubeDLSpy(urllib.request.BaseHandler):
    logger = logging.getLogger(__module__ + "." + __qualname__)

    def __init__(self):
        self.reset()

    def _http_response(self, request, response):
        txn = {
            'url': request.full_url,
            'method': request.get_method(),
            'status_code': response.code,
            'response_headers': response.headers,
        }
        self.transactions.append(txn)
        return response

    http_response = https_response = _http_response

    def reset(self):
        self.transactions = []

    def final_bounces(self, url):
        """
        Resolves redirect chains in self.transactions, returns a list of
        Transaction representing the final redirect destinations of the given
        url. There could be more than one if for example youtube-dl hit the
        same url with HEAD and then GET requests.
        """
        redirects = {}
        for txn in self.transactions:
             # XXX check http status 301,302,303,307? check for "uri" header
             # as well as "location"? see urllib.request.HTTPRedirectHandler
             if 'location' in txn['response_headers']:
                 redirects[txn['url']] = txn

        final_url = url
        while final_url in redirects:
            txn = redirects.pop(final_url)
            final_url = urllib.parse.urljoin(
                    txn['url'], txn['response_headers']['location'])

        final_bounces = []
        for txn in self.transactions:
            if txn['url'] == final_url:
                final_bounces.append(txn)

        return final_bounces

class BrozzlerWorker:
    logger = logging.getLogger(__module__ + "." + __qualname__)

    # 3⅓ min heartbeat interval => 10 min ttl
    # This is kind of a long time, because `frontier.claim_sites()`, which runs
    # in the same thread as the heartbeats, can take a while on a busy brozzler
    # cluster with slow rethinkdb.
    HEARTBEAT_INTERVAL = 200.0
    SITE_SESSION_MINUTES = 15

    def __init__(
            self, frontier, service_registry=None, max_browsers=1,
            chrome_exe="chromium-browser", warcprox_auto=False, proxy=None,
            skip_extract_outlinks=False, skip_visit_hashtags=False,
            skip_youtube_dl=False, page_timeout=300, behavior_timeout=900):
        self._frontier = frontier
        self._service_registry = service_registry
        self._max_browsers = max_browsers

        self._warcprox_auto = warcprox_auto
        self._proxy = proxy
        assert not (warcprox_auto and proxy)
        self._proxy_is_warcprox = None
        self._skip_extract_outlinks = skip_extract_outlinks
        self._skip_visit_hashtags = skip_visit_hashtags
        self._skip_youtube_dl = skip_youtube_dl
        self._page_timeout = page_timeout
        self._behavior_timeout = behavior_timeout

        self._browser_pool = brozzler.browser.BrowserPool(
                max_browsers, chrome_exe=chrome_exe, ignore_cert_errors=True)
        self._browsing_threads = set()
        self._browsing_threads_lock = threading.Lock()

        self._thread = None
        self._start_stop_lock = threading.Lock()
        self._shutdown = threading.Event()

    def _choose_warcprox(self):
        warcproxes = self._service_registry.available_services('warcprox')
        if not warcproxes:
            return None
        reql = self._frontier.rr.table('sites').between(
                ['ACTIVE', r.minval], ['ACTIVE', r.maxval],
                index='sites_last_disclaimed')
        active_sites = list(reql.run())
        for warcprox in warcproxes:
            address = '%s:%s' % (warcprox['host'], warcprox['port'])
            warcprox['assigned_sites'] = len([
                site for site in active_sites
                if 'proxy' in site and site['proxy'] == address])
        warcproxes.sort(key=lambda warcprox: (
            warcprox['assigned_sites'], warcprox['load']))
        # XXX make this heuristic more advanced?
        return warcproxes[0]

    def _proxy_for(self, site):
        if self._proxy:
            return self._proxy
        elif site.proxy:
            return site.proxy
        elif self._warcprox_auto:
            svc = self._choose_warcprox()
            if svc is None:
                raise brozzler.ProxyError(
                        'no available instances of warcprox in the service '
                        'registry')
            site.proxy = '%s:%s' % (svc['host'], svc['port'])
            site.save()
            self.logger.info(
                    'chose warcprox instance %r from service registry for %r',
                    site.proxy, site)
            return site.proxy
        return None

    def _using_warcprox(self, site):
        if self._proxy:
            if self._proxy_is_warcprox is None:
                try:
                    response = requests.get('http://%s/status' % self._proxy)
                    status = json.loads(response.text)
                    self._proxy_is_warcprox = (status['role'] == 'warcprox')
                except Exception as e:
                    self._proxy_is_warcprox = False
                logging.info(
                        '%s %s warcprox', self._proxy,
                        'IS' if self._proxy_is_warcprox else 'IS NOT')
            return self._proxy_is_warcprox
        else:
            return bool(site.proxy or self._warcprox_auto)


    def _youtube_dl(self, destdir, site):
        def ydl_progress(*args, **kwargs):
            # in case youtube-dl takes a long time, heartbeat site.last_claimed
            # to prevent another brozzler-worker from claiming the site
            try:
                if site.rr and doublethink.utcnow() - site.last_claimed > datetime.timedelta(minutes=self.SITE_SESSION_MINUTES):
                    self.logger.debug(
                            'heartbeating site.last_claimed to prevent another '
                            'brozzler-worker claiming this site id=%r', site.id)
                    site.last_claimed = doublethink.utcnow()
                    site.save()
            except:
                self.logger.debug(
                        'problem heartbeating site.last_claimed site id=%r',
                        site.id, exc_info=True)

        ydl_opts = {
            "outtmpl": "{}/ydl%(autonumber)s.out".format(destdir),
            "verbose": False,
            "retries": 1,
            "logger": logging.getLogger("youtube_dl"),
            "nocheckcertificate": True,
            "hls_prefer_native": True,
            "noprogress": True,
            "nopart": True,
            "no_color": True,
            "progress_hooks": [ydl_progress],
             # https://github.com/rg3/youtube-dl/blob/master/README.md#format-selection
             # "best: Select the best quality format represented by a single
             # file with video and audio."
            "format": "best/bestvideo+bestaudio",
        }
        if self._proxy_for(site):
            ydl_opts["proxy"] = "http://{}".format(self._proxy_for(site))
            ## XXX (sometimes?) causes chrome debug websocket to go through
            ## proxy. Maybe not needed thanks to hls_prefer_native.
            ## # see https://github.com/rg3/youtube-dl/issues/6087
            ## os.environ["http_proxy"] = "http://{}".format(self._proxy_for(site))
        ydl = youtube_dl.YoutubeDL(ydl_opts)
        if site.extra_headers():
            ydl._opener.add_handler(ExtraHeaderAdder(site.extra_headers()))
        ydl.brozzler_spy = YoutubeDLSpy()
        ydl._opener.add_handler(ydl.brozzler_spy)
        return ydl

    def _warcprox_write_record(
            self, warcprox_address, url, warc_type, content_type,
            payload, extra_headers=None):
        headers = {"Content-Type":content_type,"WARC-Type":warc_type,"Host":"N/A"}
        if extra_headers:
            headers.update(extra_headers)
        request = urllib.request.Request(url, method="WARCPROX_WRITE_RECORD",
                headers=headers, data=payload)

        # XXX setting request.type="http" is a hack to stop urllib from trying
        # to tunnel if url is https
        request.type = "http"
        request.set_proxy(warcprox_address, "http")

        try:
            with urllib.request.urlopen(request, timeout=600) as response:
                if response.getcode() != 204:
                    self.logger.warn(
                            'got "%s %s" response on warcprox '
                            'WARCPROX_WRITE_RECORD request (expected 204)',
                            response.getcode(), response.reason)
        except urllib.error.HTTPError as e:
            self.logger.warn(
                    'got "%s %s" response on warcprox '
                    'WARCPROX_WRITE_RECORD request (expected 204)',
                    e.getcode(), e.info())
        except urllib.error.URLError as e:
            raise brozzler.ProxyError(
                    'proxy error on WARCPROX_WRITE_RECORD %s' % url) from e
        except ConnectionError as e:
            raise brozzler.ProxyError(
                    'proxy error on WARCPROX_WRITE_RECORD %s' % url) from e

    def _remember_videos(self, page, ydl_spy):
        if not 'videos' in page:
            page.videos = []
        for txn in ydl_spy.transactions:
            content_type = txn['response_headers'].get_content_type()
            if (content_type.startswith('video/')
                    # skip manifests of DASH segmented video -
                    # see https://github.com/internetarchive/brozzler/pull/70
                    and content_type != 'video/vnd.mpeg.dash.mpd'
                    and txn['method'] == 'GET'
                    and txn['status_code'] in (200, 206)):
                video = {
                    'blame': 'youtube-dl',
                    'url': txn['url'],
                    'response_code': txn['status_code'],
                    'content-type': content_type,
                }
                if 'content-length' in txn['response_headers']:
                    video['content-length'] = int(
                            txn['response_headers']['content-length'])
                if 'content-range' in txn['response_headers']:
                    video['content-range'] = txn[
                            'response_headers']['content-range']
                logging.debug('embedded video %s', video)
                page.videos.append(video)

    def _try_youtube_dl(self, ydl, site, page):
        try:
            self.logger.info("trying youtube-dl on {}".format(page))

            with brozzler.thread_accept_exceptions():
                # we do whatwg canonicalization here to avoid "<urlopen error
                # no host given>" resulting in ProxyError
                # needs automated test
                info = ydl.extract_info(str(urlcanon.whatwg(page.url)))
            self._remember_videos(page, ydl.brozzler_spy)
            # logging.info('XXX %s', json.dumps(info))
            if self._using_warcprox(site):
                info_json = json.dumps(info, sort_keys=True, indent=4)
                self.logger.info(
                        "sending WARCPROX_WRITE_RECORD request to warcprox "
                        "with youtube-dl json for %s", page)
                self._warcprox_write_record(
                        warcprox_address=self._proxy_for(site),
                        url="youtube-dl:%s" % str(urlcanon.semantic(page.url)),
                        warc_type="metadata",
                        content_type="application/vnd.youtube-dl_formats+json;charset=utf-8",
                        payload=info_json.encode("utf-8"),
                        extra_headers=site.extra_headers())
        except brozzler.ShutdownRequested as e:
            raise
        except BaseException as e:
            if hasattr(e, "exc_info") and e.exc_info[0] == youtube_dl.utils.UnsupportedError:
                pass
            elif (hasattr(e, "exc_info")
                    and e.exc_info[0] == urllib.error.HTTPError
                    and hasattr(e.exc_info[1], "code")
                    and e.exc_info[1].code == 420):
                raise brozzler.ReachedLimit(e.exc_info[1])
            elif (hasattr(e, 'exc_info')
                    and e.exc_info[0] == urllib.error.URLError
                    and self._proxy_for(site)):
                # connection problem when using a proxy == proxy error (XXX?)
                raise brozzler.ProxyError(
                        'youtube-dl hit apparent proxy error from '
                        '%s' % page.url) from e
            else:
                raise

    def full_and_thumb_jpegs(self, large_png):
        # these screenshots never have any alpha (right?)
        img = PIL.Image.open(io.BytesIO(large_png)).convert('RGB')

        out = io.BytesIO()
        img.save(out, "jpeg", quality=95)
        full_jpeg = out.getbuffer()

        thumb_width = 300
        thumb_height = (thumb_width / img.size[0]) * img.size[1]
        img.thumbnail((thumb_width, thumb_height))
        out = io.BytesIO()
        img.save(out, "jpeg", quality=95)
        thumb_jpeg = out.getbuffer()

        return full_jpeg, thumb_jpeg

    def brozzle_page(self, browser, site, page, on_screenshot=None,
                     on_request=None, enable_youtube_dl=True):
        self.logger.info("brozzling {}".format(page))
        if enable_youtube_dl:
            try:
                with tempfile.TemporaryDirectory(prefix='brzl-ydl-') as tempdir:
                    ydl = self._youtube_dl(tempdir, site)
                    ydl_spy = ydl.brozzler_spy # remember for later
                    self._try_youtube_dl(ydl, site, page)
            except brozzler.ReachedLimit as e:
                raise
            except brozzler.ShutdownRequested:
                raise
            except brozzler.ProxyError:
                raise
            except Exception as e:
                if (hasattr(e, 'exc_info') and len(e.exc_info) >= 2
                        and hasattr(e.exc_info[1], 'code')
                        and e.exc_info[1].code == 430):
                    self.logger.info(
                            'youtube-dl got %s %s processing %s',
                            e.exc_info[1].code, e.exc_info[1].msg, page.url)
                else:
                    self.logger.error(
                            'youtube_dl raised exception on %s', page,
                            exc_info=True)
        else:
            ydl_spy = False

        if self._needs_browsing(page, ydl_spy):
            self.logger.info('needs browsing: %s', page)
            outlinks = self._browse_page(browser, site, page, on_screenshot,
                                         on_request)
            return outlinks
        else:
            if not self._already_fetched(page, ydl_spy):
                self.logger.info('needs fetch: %s', page)
                self._fetch_url(site, page)
            else:
                self.logger.info('already fetched: %s', page)
            return []

    def _browse_page(self, browser, site, page, on_screenshot=None, on_request=None):
        def _on_screenshot(screenshot_png):
            if on_screenshot:
                on_screenshot(screenshot_png)
            if self._using_warcprox(site):
                self.logger.info(
                        "sending WARCPROX_WRITE_RECORD request to %s with "
                        "screenshot for %s", self._proxy_for(site), page)
                screenshot_jpeg, thumbnail_jpeg = self.full_and_thumb_jpegs(
                        screenshot_png)
                self._warcprox_write_record(
                        warcprox_address=self._proxy_for(site),
                        url="screenshot:%s" % str(urlcanon.semantic(page.url)),
                        warc_type="resource", content_type="image/jpeg",
                        payload=screenshot_jpeg,
                        extra_headers=site.extra_headers())
                self._warcprox_write_record(
                        warcprox_address=self._proxy_for(site),
                        url="thumbnail:%s" % str(urlcanon.semantic(page.url)),
                        warc_type="resource", content_type="image/jpeg",
                        payload=thumbnail_jpeg,
                        extra_headers=site.extra_headers())

        def _on_response(chrome_msg):
            if ('params' in chrome_msg
                    and 'response' in chrome_msg['params']
                    and 'mimeType' in chrome_msg['params']['response']
                    and chrome_msg['params']['response'].get('mimeType', '').startswith('video/')
                    # skip manifests of DASH segmented video -
                    # see https://github.com/internetarchive/brozzler/pull/70
                    and chrome_msg['params']['response']['mimeType'] != 'video/vnd.mpeg.dash.mpd'
                    and chrome_msg['params']['response'].get('status') in (200, 206)):
                video = {
                    'blame': 'browser',
                    'url': chrome_msg['params']['response'].get('url'),
                    'response_code': chrome_msg['params']['response']['status'],
                    'content-type': chrome_msg['params']['response']['mimeType'],
                }
                response_headers = CaseInsensitiveDict(
                        chrome_msg['params']['response']['headers'])
                if 'content-length' in response_headers:
                    video['content-length'] = int(response_headers['content-length'])
                if 'content-range' in response_headers:
                    video['content-range'] = response_headers['content-range']
                logging.debug('embedded video %s', video)
                if not 'videos' in page:
                    page.videos = []
                page.videos.append(video)

        if not browser.is_running():
            browser.start(
                    proxy=self._proxy_for(site),
                    cookie_db=site.get('cookie_db'))
        final_page_url, outlinks = browser.browse_page(
                page.url, extra_headers=site.extra_headers(),
                behavior_parameters=site.get('behavior_parameters'),
                username=site.get('username'), password=site.get('password'),
                user_agent=site.get('user_agent'),
                on_screenshot=_on_screenshot, on_response=_on_response,
                on_request=on_request, hashtags=page.hashtags,
                skip_extract_outlinks=self._skip_extract_outlinks,
                skip_visit_hashtags=self._skip_visit_hashtags,
                skip_youtube_dl=self._skip_youtube_dl,
                page_timeout=self._page_timeout,
                behavior_timeout=self._behavior_timeout)
        if final_page_url != page.url:
            page.note_redirect(final_page_url)
        return outlinks

    def _fetch_url(self, site, page):
        proxies = None
        if self._proxy_for(site):
            proxies = {
                'http': 'http://%s' % self._proxy_for(site),
                'https': 'http://%s' % self._proxy_for(site),
            }

        self.logger.info('fetching %s', page)
        try:
            # response is ignored
            requests.get(
                    page.url, proxies=proxies, headers=site.extra_headers(),
                    verify=False)
        except requests.exceptions.ProxyError as e:
            raise brozzler.ProxyError(
                    'proxy error fetching %s' % page.url) from e

    def _needs_browsing(self, page, brozzler_spy):
        if brozzler_spy:
            final_bounces = brozzler_spy.final_bounces(page.url)
            if not final_bounces:
                return True
            for txn in final_bounces:
                if txn['response_headers'].get_content_type() in [
                        'text/html', 'application/xhtml+xml']:
                    return True
            return False
        else:
            return True

    def _already_fetched(self, page, brozzler_spy):
        if brozzler_spy:
            for txn in brozzler_spy.final_bounces(page.url):
                if (txn['method'] == 'GET' and txn['status_code'] == 200):
                    return True
        return False

    def brozzle_site(self, browser, site):
        try:
            site.last_claimed_by = '%s:%s' % (
                    socket.gethostname(), browser.chrome.port)
            site.save()
            start = time.time()
            page = None
            self._frontier.enforce_time_limit(site)
            self._frontier.honor_stop_request(site)
            # _proxy_for() call in log statement can raise brozzler.ProxyError
            # which is why we honor time limit and stop request first☝🏻
            self.logger.info(
                    "brozzling site (proxy=%r) %r",
                    self._proxy_for(site), site)
            while time.time() - start < self.SITE_SESSION_MINUTES * 60:
                site.refresh()
                self._frontier.enforce_time_limit(site, time.time() - start)
                self._frontier.honor_stop_request(site)
                page = self._frontier.claim_page(site, "%s:%s" % (
                    socket.gethostname(), browser.chrome.port))

                if (page.needs_robots_check and
                        not brozzler.is_permitted_by_robots(
                            site, page.url, self._proxy_for(site))):
                    logging.warn("page %s is blocked by robots.txt", page.url)
                    page.blocked_by_robots = True
                    self._frontier.completed_page(site, page)
                else:
                    outlinks = self.brozzle_page(
                            browser, site, page,
                            enable_youtube_dl=not self._skip_youtube_dl)
                    self._frontier.completed_page(site, page)
                    self._frontier.scope_and_schedule_outlinks(
                            site, page, outlinks)
                    if browser.is_running():
                        site.cookie_db = browser.chrome.persist_and_read_cookie_db()

                page = None
        except brozzler.ShutdownRequested:
            self.logger.info("shutdown requested")
        except brozzler.NothingToClaim:
            self.logger.info("no pages left for site %s", site)
        except brozzler.ReachedLimit as e:
            self._frontier.reached_limit(site, e)
        except brozzler.ReachedTimeLimit as e:
            self._frontier.finished(site, "FINISHED_TIME_LIMIT")
        except brozzler.CrawlStopped:
            self._frontier.finished(site, "FINISHED_STOP_REQUESTED")
        # except brozzler.browser.BrowsingAborted:
        #     self.logger.info("{} shut down".format(browser))
        except brozzler.ProxyError as e:
            if self._warcprox_auto:
                logging.error(
                        'proxy error (site.proxy=%s), will try to choose a '
                        'healthy instance next time site is brozzled: %s',
                        site.proxy, e)
                site.proxy = None
            else:
                # using brozzler-worker --proxy, nothing to do but try the
                # same proxy again next time
                logging.error(
                        'proxy error (site.proxy=%r): %r', site.proxy, e)
        except:
            self.logger.critical("unexpected exception", exc_info=True)
        finally:
            if start:
                site.active_brozzling_time = (site.active_brozzling_time or 0) + time.time() - start
            self._frontier.disclaim_site(site, page)

    def _brozzle_site_thread_target(self, browser, site):
        try:
            self.brozzle_site(browser, site)
        finally:
            browser.stop()
            self._browser_pool.release(browser)
            with self._browsing_threads_lock:
                self._browsing_threads.remove(threading.current_thread())

    def _service_heartbeat(self):
        if hasattr(self, "status_info"):
            status_info = self.status_info
        else:
            status_info = {
                "role": "brozzler-worker",
                "ttl": self.HEARTBEAT_INTERVAL * 3,
            }
        status_info["load"] = 1.0 * self._browser_pool.num_in_use() / self._browser_pool.size
        status_info["browser_pool_size"] = self._browser_pool.size
        status_info["browsers_in_use"] = self._browser_pool.num_in_use()

        try:
            self.status_info = self._service_registry.heartbeat(status_info)
            self.logger.trace(
                    "status in service registry: %s", self.status_info)
        except r.ReqlError as e:
            self.logger.error(
                    "failed to send heartbeat and update service registry "
                    "with info %s: %s", status_info, e)

    def _service_heartbeat_if_due(self):
        '''Sends service registry heartbeat if due'''
        due = False
        if self._service_registry:
            if not hasattr(self, "status_info"):
                due = True
            else:
                d = doublethink.utcnow() - self.status_info["last_heartbeat"]
                due = d.total_seconds() > self.HEARTBEAT_INTERVAL

        if due:
            self._service_heartbeat()

    def _start_browsing_some_sites(self):
        '''
        Starts browsing some sites.

        Raises:
            NoBrowsersAvailable if none available
        '''
        browsers = self._browser_pool.acquire_multi(
                (self._browser_pool.num_available() + 1) // 2)
        try:
            sites = self._frontier.claim_sites(len(browsers))
        except:
            self._browser_pool.release_all(browsers)
            raise

        for i in range(len(browsers)):
            if i < len(sites):
                th = threading.Thread(
                        target=self._brozzle_site_thread_target,
                        args=(browsers[i], sites[i]),
                        name="BrozzlingThread:%s" % browsers[i].chrome.port,
                        daemon=True)
                with self._browsing_threads_lock:
                    self._browsing_threads.add(th)
                th.start()
            else:
                self._browser_pool.release(browsers[i])

    def run(self):
        self.logger.info("brozzler worker starting")
        try:
            while not self._shutdown.is_set():
                self._service_heartbeat_if_due()
                try:
                    self._start_browsing_some_sites()
                except brozzler.browser.NoBrowsersAvailable:
                    logging.trace(
                            "all %s browsers are in use", self._max_browsers)
                except brozzler.NothingToClaim:
                    logging.trace(
                            "all active sites are already claimed by a "
                            "brozzler worker")
                time.sleep(0.5)

            self.logger.info("shutdown requested")
        except r.ReqlError as e:
            self.logger.error(
                    "caught rethinkdb exception, will try to proceed",
                    exc_info=True)
        except brozzler.ShutdownRequested:
            self.logger.info("shutdown requested")
        except:
            self.logger.critical(
                    "thread exiting due to unexpected exception",
                    exc_info=True)
        finally:
            if self._service_registry and hasattr(self, "status_info"):
                try:
                    self._service_registry.unregister(self.status_info["id"])
                except:
                    self.logger.error(
                            "failed to unregister from service registry",
                            exc_info=True)

            self.logger.info(
                    'shutting down %s brozzling threads',
                    len(self._browsing_threads))
            with self._browsing_threads_lock:
                for th in self._browsing_threads:
                    if th.is_alive():
                        brozzler.thread_raise(th, brozzler.ShutdownRequested)
            self._browser_pool.shutdown_now()
            # copy to avoid "RuntimeError: Set changed size during iteration"
            thredz = set(self._browsing_threads)
            for th in thredz:
                th.join()

    def start(self):
        with self._start_stop_lock:
            if self._thread:
                self.logger.warn(
                        'ignoring start request because self._thread is '
                        'not None')
                return
            self._thread = threading.Thread(
                    target=self.run, name="BrozzlerWorker")
            self._thread.start()

    def shutdown_now(self):
        self.stop()

    def stop(self):
        self._shutdown.set()

    def is_alive(self):
        return self._thread and self._thread.is_alive()

