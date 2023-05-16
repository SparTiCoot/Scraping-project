import requests
from bs4 import BeautifulSoup
import pandas as pd


NB_POKEMON_MAX = 50
EXPORT_PATH = "./exports/"


class Pokemon:

    def __init__(self, number='', form='', french_name='', english_name='', types=[], ) -> None:
        self.number = number
        self.form = form
        self.french_name = french_name
        self.english_name = english_name
        self.types = types

    def show_all_pokemon(self):
        print(f"Numéro du Pokémon: {self.number}")
        if self.form != "":
            print(f"Forme: {self.form}")
        print(
            f"Nom en Français: {self.french_name}, en Anglais: {self.english_name}")
        print("Type(s): ")
        for type in self.types:
            print(type)


def main():
    url = "https://www.pokepedia.fr/Liste_des_Pok%C3%A9mon_dans_l%27ordre_du_Pok%C3%A9dex_National"

    soup = BeautifulSoup()
    data = requests.get(url).text

    soup = BeautifulSoup(data, 'html.parser')

    # for table in soup.find_all('table'):
    #     print(table.get('class'))

    types = []
    table = soup.find('table', class_='tableaustandard sortable entetefixe')
    form = ""
    list_of_pokemon = []
    for row in table.tbody.find_all('tr'):
        columns = row.find_all('td')
        types = [type['alt'] for type in columns[-1].find_all('img')]
        if columns[2].small != None:
            form = columns[2].small.text
        if columns[0].text != "":
            number = columns[0].text
            list_of_pokemon.append(
                Pokemon(number, form, columns[2].a.text, columns[3].a.text, types))
        if columns[0].text == "":
            list_of_pokemon.append(
                Pokemon(number, form, columns[2].a.text, columns[3].a.text, types))
        form = ""

    for pokemon in list_of_pokemon:
        pokemon.show_all_pokemon()


if __name__ == "__main__":
    main()
