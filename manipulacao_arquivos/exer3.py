import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.avis.com/pt/cars/vehicles/us/k")
soup = BeautifulSoup(url.text, "html.parser")


paragrafos = soup.find_all('p')

print(paragrafos)

for paragrafo in paragrafos:
    paragrafo = paragrafo.text.strip()
    if paragrafo != "":
        print(paragrafo)