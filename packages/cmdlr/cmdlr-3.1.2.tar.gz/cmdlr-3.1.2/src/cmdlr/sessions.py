"""Cmdlr clawler subsystem."""

import asyncio
import random
import collections
import urllib.parse as UP
import sys

import aiohttp

from . import amgr
from . import info
from . import config
from . import log


_DYN_DELAY_TABLE = {  # dyn_delay_factor -> second
    0: 0,
    1: 5,
    2: 10,
    3: 20,
    4: 30,
    5: 40,
    6: 50,
    7: 60,
    8: 90,
    9: 120,
    10: 180,
    11: 240,
    12: 300,
    13: 600,
    14: 900,
    15: 1200,
    16: 1500,
    17: 1800,
    18: 2100,
    19: 2400,
    20: 3600,
}


_per_host_semaphore_factory = None


def _get_default_host():
    return {'dyn_delay_factor': 0,
            'semaphore': _per_host_semaphore_factory()}


_session_pool = {}
_host_pool = collections.defaultdict(_get_default_host)
_loop = None
_semaphore = None


def _get_session_init_kwargs(analyzer):
    analyzer_kwargs = getattr(analyzer, 'session_init_kwargs', {})
    default_kwargs = {
        'headers': {
            'user-agent': '{}/{}'.format(info.PROJECT_NAME, info.VERSION)
        },
        'read_timeout': 120,
        'conn_timeout': 120,
    }

    kwargs = {**default_kwargs,
              **analyzer_kwargs}

    return kwargs


def _clear_session_pool():
    """Close and clear all sessions in pool."""
    for session in _session_pool.values():
        session.close()

    _session_pool.clear()


def _get_session(curl):
    """Get session from session pool by comic url."""
    analyzer = amgr.get_match_analyzer(curl)
    aname = amgr.get_analyzer_name(analyzer)

    if aname not in _session_pool:
        session_init_kwargs = _get_session_init_kwargs(analyzer)

        _session_pool[aname] = aiohttp.ClientSession(
            loop=_loop, **session_init_kwargs)

    return _session_pool[aname]


def _get_host(url):
    netloc = UP.urlparse(url).netloc

    return _host_pool[netloc]


def _get_delay_sec(dyn_delay_factor, delay):
    dyn_delay_sec = _DYN_DELAY_TABLE[dyn_delay_factor]
    static_delay_sec = random.random() * delay

    return dyn_delay_sec + static_delay_sec


def _get_dyn_delay_callbacks(host):
    dyn_delay_factor = host['dyn_delay_factor']

    def success():
        if dyn_delay_factor == host['dyn_delay_factor']:
            host['dyn_delay_factor'] = max(0, dyn_delay_factor - 1)

    def fail():
        if dyn_delay_factor == host['dyn_delay_factor']:
            host['dyn_delay_factor'] = min(20, dyn_delay_factor + 1)

    return success, fail


def init(loop):
    """Init the crawler module."""
    def per_host_semaphore_factory():
        return asyncio.Semaphore(value=config.get_per_host_concurrent(),
                                 loop=loop)

    global _loop
    _loop = loop

    global _per_host_semaphore_factory
    _per_host_semaphore_factory = per_host_semaphore_factory

    global _semaphore
    _semaphore = asyncio.Semaphore(value=config.get_max_concurrent(),
                                   loop=loop)


def close():
    """Do recycle."""
    _clear_session_pool()


def get_request(curl):
    """Get the request class."""
    session = _get_session(curl)
    proxy = config.get_proxy()
    max_try = config.get_max_retry() + 1
    delay = config.get_delay()

    class request:
        """session.request contextmanager."""

        def __init__(self, **req_kwargs):
            """init."""
            self.req_kwargs = req_kwargs
            self.host = _get_host(req_kwargs['url'])
            self.resp = None
            self.local_locked = False
            self.global_locked = False

            self.dd_success = lambda: None
            self.dd_fail = lambda: None

        async def acquire(self):
            self.local_locked = True

            await self.host['semaphore'].acquire()

            self.global_locked = True

            await _semaphore.acquire()

        def release(self):
            if self.global_locked:
                self.global_locked = False
                _semaphore.release()

            if self.local_locked:
                self.local_locked = False
                self.host['semaphore'].release()

        async def __aenter__(self):
            """Async with enter."""
            for try_idx in range(max_try):
                try:
                    await self.acquire()

                    self.dd_success, self.dd_fail = _get_dyn_delay_callbacks(
                        self.host)
                    delay_sec = _get_delay_sec(
                        self.host['dyn_delay_factor'], delay)

                    await asyncio.sleep(delay_sec)

                    self.resp = await session.request(**{
                        **{'method': 'GET', 'proxy': proxy},
                        **self.req_kwargs,
                        })
                    self.resp.raise_for_status()

                    return self.resp

                except aiohttp.ClientError as e:
                    current_try = try_idx + 1

                    log.logger.error(
                        'Request Failed ({}/{}, d{}): {} => {}: {}'
                        .format(current_try, max_try,
                                self.host['dyn_delay_factor'],
                                self.req_kwargs['url'],
                                type(e).__name__, e))

                    await self.__aexit__(*sys.exc_info())

                    if current_try == max_try:
                        raise e from None

        async def __aexit__(self, exc_type, exc, tb):
            """Async with exit."""
            if exc_type:
                if exc_type is not asyncio.CancelledError:
                    self.dd_fail()
            else:
                self.dd_success()

            if self.resp:
                await self.resp.release()

            self.release()

    return request
