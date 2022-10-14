import requests
from bs4 import BeautifulSoup as bs

def scraping_results(links_gender, names_gender):
    # Récupération des titres + dates par genre
    titres = []
    dates_de_sortie = []
    gender = []
    i = 0

    for link_gender in links_gender:
        page_gender = requests.get(link_gender)
        soup_genre = bs(page_gender.content, "html.parser")
        films = soup_genre.find_all(class_="meta-affintiy-score")

        # Boucle sur la totalité des films pour ne pas rater ceux sans date
        for film in films:
            date = film.find(class_="date")
            titre = film.find(class_="meta-title-link")
            # Ajout du genre dans le tableau pour tous les films de ce genre
            gender.append(names_gender[i])
            titres.append(titre.string)

            if date is None:
                dates_de_sortie.append("Pas de date")
            else:
                dates_de_sortie.append(date.string)
        i += 1

    return titres, dates_de_sortie, gender
