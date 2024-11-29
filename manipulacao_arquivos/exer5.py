import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://www.mercadolivre.com.br/")
soup = BeautifulSoup(url.text, "html.parser")

titlo = soup.title.string


df = pd.DataFrame({
    "Titulos":[titlo]
})
df.to_excel("planilha.xlsx", index=False)

df = pd.read_excel("planilha.xlsx")
print(df)