import aiohttp
import asyncio
from config import REQUEST_TIMEOUT

class AsyncHTTPClient:
    def __init__(self):
        timeout = aiohttp.ClientTimeout(total=REQUEST_TIMEOUT)
        connector = aiohttp.TCPConnector(limit=1000, ttl_dns_cache=300)
        self.session = aiohttp.ClientSession(
            timeout=timeout,
            connector=connector
        )

    async def fetch(self, url):
        start = asyncio.get_event_loop().time()
        async with self.session.get(url) as response:
            data = await response.json()
            latency = asyncio.get_event_loop().time() - start
            return data, latency

    async def close(self):
        await self.session.close()
