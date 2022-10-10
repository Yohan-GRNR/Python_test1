import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.allocine.fr/film/meilleurs/"

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

titres_bs = soup.find_all(class_="meta-title-link")
titres = []
for titre in titres_bs:
    titres.append(titre.string)

dates_sortie_bs = soup.find_all(class_="date")
dates_de_sortie = []
for date in dates_sortie_bs:
    dates_de_sortie.append(date.string)

entete = ["Titre", "Date de sortie"]

with open("database.csv", "w") as file_csv:
    writer = csv.writer(file_csv, delimiter=",")
    # Écrit la première ligne (l'entête)
    writer.writerow(entete)
    # Boucle les deux tableaux en quinconce
    for titre, date in zip(titres, dates_de_sortie):
        ligne=[titre, date]
        # Écrit la ligne concerné à chaque boucle
        writer.writerow(ligne)
        

#2. Attention titre sans date
