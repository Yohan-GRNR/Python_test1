import requests
from bs4 import BeautifulSoup as bs
import csv


url = "https://www.allocine.fr/film/meilleurs"
url_main = "https://www.allocine.fr"
response = requests.get(url)
soup = bs(response.content, "html.parser")

# Récupération de tous les genres (link + name)
genres = soup.find("ul", class_="filter-entity-word").find_all("a", class_="item-content", href=True)
links_gender = []
names_gender = []

for genre in genres:
    links_gender.append(url_main+genre["href"])
    names_gender.append(genre)

#######################################################

# Récupération des titres + dates par genre
titres = []
dates_de_sortie = []

for link_gender in links_gender:
    page_gender = requests.get(link_gender)
    soup_genre = bs(page_gender.content, "html.parser")


    films = soup_genre.find_all(class_="meta-affintiy-score")

# Boucle sur la totalité des films pour ne pas rater ceux sans date
    for film in films:
        date = film.find(class_="date")
        titre = film.find(class_="meta-title-link")

        titres.append(titre.string)

        if date is None:
            dates_de_sortie.append("Pas de date")
        else:
            dates_de_sortie.append(date.string)

""" --- Suivi console pour sois même ---
print(dates_de_sortie)
print(titres)
"""

# Création du tableau dans mon .csv /
entete = ["Titre", "Date de reprise"]

with open("database.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    # Écrit la première ligne (l'entête)
    writer.writerow(entete)

    # Boucle les deux tableaux en quinconce
    for titre, date in zip(titres, dates_de_sortie):
        ligne = [titre, date]
        # Écrit la ligne concerné à chaque boucle
        writer.writerow(ligne)
