from typing import Any
import requests
import csv
import os
from bs4 import BeautifulSoup
import pandas as pd


NB_POKEMON_MAX = 50

def create_csv_with_data(array_of_object):
    columns = ['number', 'form', 'french_name', 'english_name', 'types']

    os.makedirs("data", exist_ok=True)
    path_file_csv = 'data/pokemons.csv'
    with open(path_file_csv, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        for object in array_of_object:
            types_str = ','.join(object.types)
            writer.writerow({columns[0]: object.number, columns[1]: object.form, columns[2]: object.french_name, columns[3]: object.english_name, columns[4]: types_str})

    print("Le fichier csv a été créé avec succès.")

def convert_csv_to_excel(path_csv_file, path_excel_file):
    data_frame = pd.read_csv(path_csv_file)
    data_frame.to_excel(path_excel_file, index=False)

    print("Le fichier excel a été créé avec succès.")


class Pokemon:

    def __init__(self, number='', form='', french_name='', english_name='', types=[]) -> None:
        self.number = number
        self.form = form
        self.french_name = french_name
        self.english_name = english_name
        self.types = types

    def __str__(self) -> str:
        if self.form == "":
            return f"Numéro du Pokémon: {str(self.number)}, Nom en Français: {self.french_name}, en Anglais: {self.english_name}, Type(s): {self.types}"
        else:
            return f"Numéro du Pokémon: {str(self.number)}, Forme: {self.form}, Nom en Français: {self.french_name}, en Anglais: {self.english_name}, Type(s): {self.types}"

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

def main() -> None:
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

    # for pokemon in list_of_pokemon:
        # print(pokemon)
        # print(pokemon.form)

    # create_csv_with_data(list_of_pokemon)
    # convert_csv_to_excel('data/pokemons.csv', 'data/pokemons.xlsx')

if __name__ == "__main__":
    main()
