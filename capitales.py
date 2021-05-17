# coding: UTF-8
"""
Script: Prog_Python/capitales.py
Création: frederic, le 06/04/2021
"""


# Imports
import json
import random


# Fonctions
def capitales():
    #with open('D:/Documents/Prog_Python/TP10/data/europe.json') as json_data:
    with open('tests/data/europe.json') as json_data:
            europe = json.load(json_data)
    return europe


def affichage_capitales(dico):
    for pays in dico:
        print(dico[pays]) #affichage ligne par ligne des capitales


def affichage_capitales_triees(dico):
    liste_capitales = sorted(dict.values(dico)) #trie les valeur du dictionnaire par ordre alphabetique
    print(liste_capitales)


def choix_pays_aleatoire(dictionnaire):
    liste_pays =list(dictionnaire) # list(dic) retourne la liste des clefs du dico
    pays = random.choice(liste_pays) # retourne une valeur aléatoire d'une liste
    return pays


def choix_reponses_possibles(pays, dictionnaire):
    dico_local = {pays:dictionnaire[pays]} # initialisation du dico des propositions
    nombre = 0
    while nombre<3:
        pays_test = choix_pays_aleatoire(dictionnaire)
        if pays_test not in dico_local:
            dico_local[pays_test] = dictionnaire[pays_test]
            nombre += 1
    return dico_local


def une_question(dictionnaire, pays):
    print("Quelle est la capitale de {}".format(pays))
    liste_prop = choix_reponses_possibles(pays, dictionnaire)
    affichage_capitales_triees(liste_prop)
    print("Quelle est votre réponse ?")
    chaine = input()
    if chaine == dictionnaire[pays]:
        return True
    else:
        return False


# Programme principal
def main():
    europe = capitales()

    pays = choix_pays_aleatoire(europe)
    print(une_question(europe, pays))

if __name__ == '__main__':
    main()
# Fin
