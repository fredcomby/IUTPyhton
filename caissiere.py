# coding: UTF-8
"""
Script: Prog_Python/caissiere.py
Création: frederic, le 19/03/2021
"""

# Imports
import tools_caissiere
import math


# Fonctions
def affiche_prix(liste):
    print("Détails des articles:")
    for i in range(len(liste)):
        print("article {}: {}€".format((i + 1), liste[i]))
    return None


def calcul_montant(liste):
    montant = 0
    for i in range(len(liste)):
        montant += liste[i]
    return montant


def calcul_montant_avec_remise(liste, seuil, taux):
    montant = 0
    for i in range(len(liste)):
        if liste[i] > seuil:
            montant += liste[i] * (100 - taux) / 100
        else:
            montant += liste[i]
    return math.floor(montant)


def calcul_montant_a_rendre(montant_du):
    return 500 - montant_du


def affiche_monnaie(montant):
    coupures = [100, 50, 20, 10, 5, 2, 1]
    resultat = "Montant à rendre sur 500€: {}€, soit ".format(montant)
    for i in range(len(coupures)):
        nb = montant // coupures[i]
        montant -= nb * coupures[i]
        resultat += "{} * {}€ ".format(nb, coupures[i])
        if i != (len(coupures)-1):
            resultat += "+ "
    print(resultat)
    return None


# Programme principal
def main():
    liste = tools_caissiere.get_liste_prix()
    affiche_prix(liste)
    montant_avec_remise = calcul_montant_avec_remise(liste, 10, 20)
    print("Total facturé (après remise): {}€".format(montant_avec_remise))
    montant_du = calcul_montant_a_rendre(montant_avec_remise)
    affiche_monnaie(montant_du)


if __name__ == '__main__':
    main()
# Fin
