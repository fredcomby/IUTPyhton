# coding: UTF-8
"""
Script: Prog_Pyhton/date.py
Création: frederic, le 17/03/2021
"""

# Imports
import random
import tools_date


# Fonctions
def est_valide(jour, mois, annee):
    if annee < 1583:
        return False

    if (mois < 1) | (mois > 12):
        return False

    # tests sur le nombre de jours du mois
    if (mois == 1) | (mois == 3) | (mois == 5) | (mois == 7) | (mois == 8) | (mois == 10) | (mois == 12):
        if (jour < 1) | (jour > 31):
            return False
    elif mois == 2:  # mois de février
        if ((annee % 4 == 0) & (annee % 100 != 0)) | (annee % 400 == 0):  # année bissextile
            if (jour < 1) | (jour > 29):
                return False
        else:
            if (jour < 1) | (jour > 28):
                return False
    else:
        if (jour < 1) | (jour > 30):
            return False
    return True


def get_jour_semaine(jour, mois, annee):
    nombre = int(tools_date.get_numero_jour_semaine(jour, mois, annee))
    table_jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]
    return table_jours[nombre]


# Programme principal
def main():
    annee = 2030
    jour = random.randint(1, 40)
    mois = random.randint(1, 15)

    if est_valide(jour, mois, annee):
        print("Le {}/{}/{} est un {}.".format(jour, mois, annee, get_jour_semaine(jour, mois, annee)))
    else:
        print("Le {}/{}/{} n'est pas une date valide.".format(jour, mois, annee))


if __name__ == '__main__':
    main()
# Fin
