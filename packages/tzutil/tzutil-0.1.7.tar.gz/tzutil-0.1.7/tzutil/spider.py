#!/usr/bin/env python
import json
import aiohttp
import asyncio
from urllib.parse import urlparse,ParseResult,parse_qsl,parse_qs
from tzutil.ob import Ob

class Req:
    def __init__(self, url, html):
        self.__url = url
        self.text = html

    @property
    def ob(self):
        o = self.json
        return (Ob()<<o)

    @property
    def json(self):
        return json.loads(self.text)

    @property
    def parse_qs(self):
        return parse_qs(self.__url.query)

    @property
    def parse_qsl(self):
        return parse_qsl(self.__url.query)

    def __getattr__(self, attr):
        return getattr(self.__url, attr)

class Spider:
    def __init__(self, duration=20):
        self._todo = []
        self._timeout = 60
        self._costed = 0
        self._duration = 20
        self._func = []

    def get(self, url):
        self._todo.append(url)

    async def _get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def _run(self):
        duration = self._duration
        while 1:
            if self._todo:
                url = self._todo.pop()
                html = await self._get(url)
                self._parse(url, html)
            else:
                if self._costed > self._timeout:
                    return
                self._costed += duration
                print('队列为空 %s秒'%self._costed)
            await asyncio.sleep(duration)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._run())

    def _parse(self, url, html):
        url = urlparse(url)
        for pattern, func in self._func:
            p = pattern.get('path')
            if p:
                path = url.path[1:]
                pathb = path.encode('utf-8')
                if type(p) is bytes:
                    if pathb == p:
                        func(Req(url,html))

    def __call__(self, **kwds):
        def _(func):
            self._func.append((kwds, func))
            return func
        return _

