import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
# Permet d'atteindre la page
response = requests.get(url)
page = response.content
# Permet de traduire le contenu (content) de la page (response) grace au parser HTML
soup = BeautifulSoup(page, "html.parser")

#Scanner les <a> avec ce nom de class
titres_articles = soup.find_all("a", class_="gem-c-document-list__item-title")

#Créer tableau avec uniquement le texte (.string)
liste_titres = []
for titre_article in titres_articles:
    liste_titres.append(titre_article.string)

descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
liste_descriptions = []
for description in descriptions:
    liste_descriptions.append( description.string )

print(liste_titres, liste_descriptions )