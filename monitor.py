import asyncio
from config import BASE_URL, CONCURRENT_REQUESTS, MONITOR_INTERVAL
from client import AsyncHTTPClient
from stats import Stats

async def monitor():
    client = AsyncHTTPClient()
    stats = Stats()

    while True:
        tasks = [
            client.fetch(BASE_URL)
            for _ in range(CONCURRENT_REQUESTS)
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):
                continue
            data, latency = result
            stats.update(latency)

        print(stats.report())
        await asyncio.sleep(MONITOR_INTERVAL)
