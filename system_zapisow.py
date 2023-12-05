# POST /login.php HTTP/1.1
# Host: zapisy.ii.uni.wroc.pl
# User-Agent: Mozilla/5.0
# username=ja&password=hasło

from requests import Session

url = "https://zapisy.ii.uni.wroc.pl/"

cred = {"username": "291545@uwr.edu.pl", "password": "qwaszx[]12"}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2'}

with Session() as s:
    s.get(url, headers=headers)
    s.post(url + "users/login", data=cred, headers=headers)
    odp = s.get(url + "news/", headers=headers)
    print(odp.text)