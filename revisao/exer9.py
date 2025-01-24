import requests
from bs4 import BeautifulSoup

url = requests.get('https://ge.globo.com/')
soup = BeautifulSoup(url.text, "html.parser")

titulos_h1 = soup.find_all("h1")

for h1 in titulos_h1:
    h1 = h1.text.strip()
    print(h1)
