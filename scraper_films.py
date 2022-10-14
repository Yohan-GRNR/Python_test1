import requests
from bs4 import BeautifulSoup as bs
import csv
from fonctions.scraper import scraping_results

url = "https://www.allocine.fr/film/meilleurs"
url_main = "https://www.allocine.fr"
response = requests.get(url)
soup = bs(response.content, "html.parser")

# Récupération de tous les genres (link + name)
genres = soup.find("ul", class_="filter-entity-word").find_all("a", class_="item-content", href=True)
links_gender = []
names_gender = []

for genre in genres:
    links_gender.append(url_main + genre["href"])
    names_gender.append(genre.string)

titres, dates_de_sortie, gender = scraping_results(links_gender, names_gender)

""" --- Suivi console pour sois même ---
print(dates_de_sortie)
print(titres)
"""

# Création du tableau dans mon .csv
entete = ["Titre", "Date de reprise", "Genre"]

with open("database.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    # Écrit la première ligne (l'entête)
    writer.writerow(entete)

    # Boucle les deux tableaux en quinconce
    seen = set()
    for titre, date, genre in zip(titres, dates_de_sortie, gender):
        if titre not in seen:
            ligne = [titre, date, genre]
            writer.writerow(ligne)
            seen.add(titre)

