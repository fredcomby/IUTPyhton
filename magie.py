# coding: UTF-8
"""
Script: TP1/debuggeur.py
Création: barasc, le 19/08/2017
"""


# Imports
import tools_magie

# Fonctions
def calcul_spectateur_2021(pointure, annee_naissance):
    """Calcule la valeur magique demandée par le magicien au spectateur,
    en fonction de sa pointure et de son année de naissance, et renvoie la valeur calculée.

    Le calcul est fait en supposant que nous sommes en l'an 2021.
    """
    res = pointure
    res *= 5
    res +=50
    res *=20
    res +=1000
    res += 21
    res -= annee_naissance
    return res

def calcul_spectateur(pointure, annee_naissance):
    """Calcule la valeur magique demandée par le magicien au spectateur,
    en fonction de sa pointure et de son année de naissance, et renvoie la valeur calculée.

    Le calcul est fait en supposant que l'année est retournée par get_annee_courante().
    """
    anneeCourante = tools_magie.get_annee_courante()
    #temp = anneeCourante - int(anneeCourante/100)*100
    # le // est la division entière
    temp = anneeCourante - anneeCourante//100*100

    res = pointure
    res *= 5
    res +=50
    res *=20
    res +=1000
    res += temp
    res -= annee_naissance
    return res

def get_pointure_from_valeur(valeur_magique):
    """Calcule la pointure en fonction de la valeur magique donnée en paramètre
    """
    res = valeur_magique//100
    return res

def get_age_from_valeur(valeur_magique):
    """Calcule l'age en fonction de la valeur magique donnée en paramètre
    """
    res = valeur_magique%(get_pointure_from_valeur(valeur_magique)*100)
    return res


# Programme principal
def main():
    resultat = calcul_spectateur_2021(37, 1974)
    print("valeur magique =", resultat)
    resultat = calcul_spectateur(37, 1974)
    print("valeur magique =", resultat)

if __name__ == '__main__':
    main()
