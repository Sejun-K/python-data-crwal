import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/')
html = response.text

soup = BeautifulSoup(html, 'html.parser')

result = soup.select_one('.h_market')
print(result.text)
