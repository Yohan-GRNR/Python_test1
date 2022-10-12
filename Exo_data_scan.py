import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.allocine.fr/film/meilleurs/"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

films = soup.find_all(class_="meta-affintiy-score")
titres = []
dates_de_sortie = []

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
