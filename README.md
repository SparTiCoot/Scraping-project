# Ingénierie des Langues
# Projet Scraping - Pokédex

Projet de Scraping - Pokédex fait en binôme par OUKHEMANOU Mohand & VILFEU Vincent (L3-Y). 
Notre projet est en rapport avec la thématique : Créer un Corpus.
Elle consiste en la création d'un outil de scraping pour pouvoir extraire des données textuelles sur un site, en suivant un thème (ici les pokémons).

## Binôme
Le choix de le faire en binôme s'est fait de par le grand nombre de pages à scraper (partant du principe qu'il y aurait plus de difficulté), il était donc plus efficace de diviser le travail. 
Aussi, avec le nombre de projet important à réaliser (chacun risquant de prendre du temps), il était plus intéressant (notamment niveau gain de temps) de le faire à deux.

Vincent a commencé par l'implémentation du scraping de la première page du pokédex (celle comprenant la liste de tous les pokémons), récupérant ainsi leur numéro de pokédex, leur nom français, leur nom anglais et leurs types, via la bibliothèque BeautifulSoup. Nous permettant ainsi de remplir la database avec les pokémons dont nous voudrons récupérer les informations. 
Puis sur la base d'explications de Vincent, Mohand a implémenté le scraping des pages individuelles des pokémons, pour récupérer leur catégorie, leur taille, leur poids, leurs talents, le nombre de pas pour faire éclore leur oeuf, les EVs qu'ils rapportent, les points d'expérience qu'ils rapportent, leur expérience au niveau 100, la répartition des genres, leur couleur et leurs stats.
En corrigeant également les problèmes dû au faite que les pages n'étaient pas toutes similaires, il fallait ainsi gérer les exceptions pour éviter les problèmes d'index (lors de la récupération de certaines caractéristiques). 
De manière générale, nous relisions chacun le travail de l'autre pour échanger dessus et faire en sorte d'optimiser le code et de le rendre propre. 
Quant au rapport, il s'agissait d'un travail commun afin d'expliquer au mieux notre code. 
Nous avons travaillé via Git et nous communiquions via Discord. 

## Utilisation
Pour lancer le code (qui prendra du temps à s'exécuter (environ 5 minutes), ayant 493 pages à scraper), il faut utiliser la ligne de commande suivante : 
    python3 web_scraping.py
Le code va alors se charger de scraper toutes nos pages et de sauvegarder les informations à la fois dans un fichier csv et dans un tableur (fichier xlsx). 