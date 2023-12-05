import requests
import json

import prywatne

# url = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}'

url = 'https://api.openweathermap.org/data/2.5/weather'

# url2 = 'https://api.openweathermap.org/data/3.0/onecall'

params = {"q": "Wroclaw", "mode": "json", "units": "metric", "APPID": prywatne.ID}


res = requests.get(url, params=params)

url2 = 'https://bhagavad-gita3.p.rapidapi.com/v2/chapters/'
params2 = {"limit": "18"}


res2 = requests.get(url2, params=params2)

with open("prognoza.json", 'w') as fh:
    fh.write(json.dumps(res.json()))

with open("book.json", 'w') as fh2:
    fh2.write(json.dumps(res2.json()))