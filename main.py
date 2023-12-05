import requests
import json
import prywatne

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {"q": "Wroclaw", "mode": "json",
          "units": "metric", "APPID": prywatne.ID}

res = requests.get(url, params=params)

with open("prognoza.json", 'w') as fh:
    fh.write(json.dumps(res.json()))

url2 = "https://bhagavad-gita3.p.rapidapi.com/v2/chapters/"

params2 = {"limit":"18"}

headers = {
	"X-RapidAPI-Key": "31cd820050msh2b55af3ce4acd08p154ea8jsncc4999f8ec8c",
	"X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
}

res2 = requests.get(url2, headers=headers, params=params2)

with open('bhagavadgita.json', 'w') as fh2:
    fh2.write(json.dumps(res2.json(), ensure_ascii=False))