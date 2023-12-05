import asyncio
import aiohttp
import prywatne
import json

async def fetch_page(session, url, headers, params):
    async with session.get(url, headers=headers, params=params) as result:
        res = await result.text()
    return res

urls = ['https://api.openweathermap.org/data/2.5/weather', 'https://bhagavad-gita3.p.rapidapi.com/v2/chapters/' ]

params = [ {"q": "Wroclaw", "mode": "json",
          "units": "metric", "APPID": prywatne.ID}, {"limit":"18"} ]
headers = [ {}, {
	"X-RapidAPI-Key": "31cd820050msh2b55af3ce4acd08p154ea8jsncc4999f8ec8c",
	"X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
} ]

async def main():
    async with aiohttp.ClientSession() as session:
        requests = [fetch_page(session, loc[0], loc[1], loc[2]) for loc in zip(urls, headers, params)]
        pages = await asyncio.gather(*requests)
        with open("async_prognoza.json", 'w') as fh1:
            fh1.write(json.dumps(pages[0]))
        with open("async_bhagavadgita.json", 'w') as fh2:
            fh2.write(json.dumps(pages[1], ensure_ascii=False))


asyncio.run(main())