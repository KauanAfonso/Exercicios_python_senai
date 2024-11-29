import requests
from bs4 import BeautifulSoup


url = requests.get("https://www.avis.com/pt/cars/vehicles/us/k") 
soup = BeautifulSoup(url.text, "html.parser")
titlo = soup.title.string

print(titlo)

