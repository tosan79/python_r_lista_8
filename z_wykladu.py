# import asyncio

# async def nested():
#     return 42

# async def main():
#     nested()

#     print(await nested())

# asyncio.run(main())

####################

import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_page(session, url):
    async with session.get(url) as result:
        res = await result.text()

    return res

urls = ['https://www.ii.uni.wroc.pl', 'https://github.com', 'https://google.com']

async def main():
    async with ClientSession() as session:
        requests = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*requests)
        print([ p[100:300] for p in pages ])

asyncio.run(main())