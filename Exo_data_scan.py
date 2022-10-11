import re

import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.allocine.fr/film/meilleurs/"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

films = soup.find_all(class_="meta-affintiy-score")
regex_dates = r"<span class=\"date\">(.*)</span>"

titres = []
dates_de_sortie = []

# Boucle sur la totalité des films pour ne pas rater ceux sans date
for film in films:
    date = re.findall(regex_dates, str(film))
    # Si la valeur est null alors indiquer qu'il n'y a rien
    if not date:
        dates_de_sortie.append("Pas de date renseignée")
    else:
        dates_de_sortie.append(date)

# Chaque film a forcément un titre
titres_bs = soup.find_all(class_="meta-title-link")
for titre in titres_bs:
    titres.append(titre.string)

# Pour mon suivi -> À delete
print(titres)
print(dates_de_sortie)

# Création du tableau dans mon .csv
entete = ["Titre", "Date de reprise"]

with open("database.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    # Écrit la première ligne (l'entête)
    writer.writerow(entete)

    # Boucle les deux tableaux en quinconce
    for titre, date in zip(titres, dates_de_sortie):
        ligne=[titre, date]
        # Écrit la ligne concerné à chaque boucle
        writer.writerow(ligne)