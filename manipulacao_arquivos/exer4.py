import requests
from bs4 import BeautifulSoup

link_heref = 0
url = requests.get("https://www.mercadolivre.com.br/")
soup = BeautifulSoup(url.text, "html.parser")

link = soup.find_all('a')


for a in link:
    link_heref = a['href']
    print(f"O link é : {link_heref}")
  