import requests
from bs4 import BeautifulSoup as bs

def titles_dates_scraping(links_gender)


    for link_gender in links_gender:
       page_gender = requests.get ( link_gender )
       soup_genre = bs ( page_gender.content, "html.parser" )

films = soup_genre.find_all ( class_="meta-affintiy-score" )

titres = []
dates_de_sortie = []
# Boucle sur la totalité des films pour ne pas rater ceux sans date
for film in films:
    date = film.find ( class_="date" )
    titre = film.find ( class_="meta-title-link" )

    titres.append ( titre.string )

    if date is None:
        dates_de_sortie.append ( "Pas de date" )
    else:
        dates_de_sortie.append ( date.string )

r   eturn dates_de_sortie