import requests
from bs4 import BeautifulSoup

movieUrl = "https://entertain.naver.com/movie"

response = requests.get(movieUrl)
html = response.text

soup = BeautifulSoup(html, "html.parser")

articleTitle = soup.select("a.tit")

kwd = input("필터링 하고픈 키워드는? ")

for at in articleTitle :
    saveTitle = at.text
    if (saveTitle.count("kwd")) > 0 :
        print(saveTitle)