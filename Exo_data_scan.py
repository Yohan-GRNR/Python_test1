import requests
from bs4 import BeautifulSoup

url = "https://www.allocine.fr/film/meilleurs/"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

titres = soup.find_all(class_="meta-title-link")
for titre in titres:
    print(titre.string)

dates_sortie = soup.find_all(class_="date")
for date in dates_sortie:
    print(date.string)

#1. lier les 2 infos (colonne?)
#2. Attention titre sans date