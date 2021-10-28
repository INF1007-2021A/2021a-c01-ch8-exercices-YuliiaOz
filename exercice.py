#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Commentaires sur le cours du chapitre 8
# f.seek() intéressant pour sauter certains caractères au debut d'un fichier
"""
Il y a des espaces entre les print(f.readline()), car lit l'espace à la fin. Solution: f.readline.strip()
Pour f.readlines() ça affiche une liste de toutes les lignes du fichier
Souvent, il faut lire ligne par ligne. Pour ça, utiliser une boucle for
with open(path, 'r', encoding='utf-8') as f:
    for ine in f:
        print(line.strip())

Sinon, pour écrire:
with open(path, 'w+', encoding='utf-8') as f:
    print(f.read())
    f.write('bonjour /n allo / salut')

with open(path, 'r+', encoding='utf-8') as f:
    print(f.read())
    f.write('bonjour /n allo / salut')

file csv (comma separated ...)
import csv
import json
import pickle

def read_csv_file(path='./test.csv'):
    with open(path) as f:
        csv_reader = csv.reader(f)
        for compteur, row in enumerate(csv_reader):


csv_writer = csv.writer(f, delimiter=':')         --->  si tu veux ne pas le séparer par des virgules, mais par autre chose

def write_csv_file(path='./test.csv'):
    with open(path, mode='w', newline='') as f:
        csv_writer = csv.writer(f, delimiter=';')
        csv_writerow([..])

json (javascript ... .... ...)
utile pour transferer l'information
C'est comme un dictionnaire, mais afficher dans un fichier


def read_json_file(path='./test.json'):
    with open(path, 'r') as f:
        variable = json.load(f)
        print(variable)


def write_json_file(path='./test.json'):
    with .

fichier pickle
propre a python
écrit en format binaire
Utile pour sauvergarder un gros fichier (plus compacte a regarder et plus sécuritaire, car on peut pas regarder)
"""

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
