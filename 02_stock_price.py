import requests
from bs4 import BeautifulSoup

for stockCode in [("005930", "삼성전자"), ("373220", "엘지엔솔"), ("009830", "한화솔루션")] :
    url = f"https://finance.naver.com/item/sise.naver?code={stockCode[0]}"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    price = soup.select_one("strong#_nowVal.tah.p11")
    print(stockCode[1] + "의 가격은 : ", end="")
    print(price.text)