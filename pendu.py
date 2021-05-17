# -*- coding: UTF-8 -*-
"""
pendu.py
"""
# Import
import tools_chaines
import random

# Constantes
COUPS_MAX = 10


# fonctions
def choix_mot():
    dico = tools_chaines.liste_mots_francais()
    mot = random.choice(dico)
    return mot


def affiche_mot_un_caractere(mot, caractere):
    chaine_masquee = ""
    # parcours sur tous les caractères de chaine :
    for car in mot:
        if car == caractere:
            chaine_masquee += caractere
        else:
            chaine_masquee += "-"
    print(chaine_masquee)


def affiche_mot(mot, propositions):
    chaine_masquee = ""
    # parcours sur tous les caractères de chaine :
    for car in mot:
        if propositions.find(car) != -1:
            chaine_masquee += car
        else:
            chaine_masquee += "-"
    print(chaine_masquee)


def est_trouve(mot, lettres):
    for car in mot:
        if lettres.find(car) == -1:
            return False
    return True


def saisie(propositions):
    erreur = True
    while erreur:
        print("saisissez une lettre :")
        car = input()
        if len(car) == 1:
            if propositions.find(car) == -1:
                erreur = False

    car = car.lower()
    return car


def main():
    # Programme principal
    print(">>> Jeu du pendu <<<")
    mot = choix_mot()  # Choix du mot au hasard par l'ordinateur
    print("Mot à deviner pour debuggage :", mot)

    # Initialisations des variables de la boucle
    coup = 0  # nombre de coups joués par le joueur
    coup_perdant = 0  # nombre de coups perdant du joueur
    propositions = ""  # leta
    # tres proposées par le joueur
    partie_finie = False  # la partie est-elle finie ?

    # Boucle de jeu
    while not partie_finie:
        print("Coup n°{} (reste {} coups perdants possibles) :".format(coup, COUPS_MAX - coup_perdant))

        affiche_mot(mot, propositions)  # Affichage du mot masqué pour le joueur

        lettre = saisie(propositions)  # Choix d'une lettre
        propositions += lettre  # Ajout de la lettre au proposition
        print("lettres proposées {}".format(propositions))
        # Analyse de la lettre et conséquences sur les coups perdants
        # ...
        if mot.find(lettre) == -1:
            coup_perdant += 1

        if coup_perdant == COUPS_MAX:
            partie_finie = True

        # La partie est-elle finie ?
        if est_trouve(mot, propositions):
            partie_finie = True
        else:
            coup = coup + 1
    # Fin de la boucle de jeu

    # Analyse du jeu ? Le joueur a-t-il gagné
    if est_trouve(mot, propositions):
        print("Gagné : le mot est :", mot)
    else:
        print("Perdu : le mot était :", mot)


if __name__ == "__main__":
    main()
