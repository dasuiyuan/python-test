# -*- coding: utf-8 -*-
# @Time: 2024/12/13 14:53
# @Author: Sui Yuan
# @Software: PyCharm
# @Desc:

import asyncio
import aiohttp
import requests
import time

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "http://jagile.jd.com/myzone",
    "https://example.com",
    "https://httpbin.org/get",
    "http://jagile.jd.com/myzone"
]


async def request_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        tasks = [request_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)


def sync_fetch_all():
    return [requests.get(url).text for url in urls]


if __name__ == '__main__':
    for i in range(5):
        # 同步请求
        start = time.time()
        results = sync_fetch_all()
        print(results)
        print(f"sync cost: {time.time() - start}")

        # 异步请求
        start = time.time()
        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(fetch_all())
        # results = asyncio.run(fetch_all())
        print(results)
        print(f"async cost: {time.time() - start}")
