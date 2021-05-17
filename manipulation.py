# coding: UTF-8
"""
Script: Prog_Python/manipulation.py
Création: frederic, le 24/03/2021
"""


# Imports
import tools_chaines


# Fonctions
def affiche_debut_dictionnaire():
    liste_mots = tools_chaines.liste_mots_francais()
    for i in range(0,5,1):
        print(liste_mots[i])
    return None


def compte_mots_dictionnaire(caractere):
    liste_mots = tools_chaines.liste_mots_francais()
    compteur = 0
    for i in range(len(liste_mots)):
#        chaine = liste_mots[i]
#        chaine.startswith(caractere)
#        a tester ...

        if str.startswith(liste_mots[i],caractere):
            compteur +=1
    return compteur


def affiche_mots_avec_caractere(caractere, nombre):
    liste_mots = tools_chaines.liste_mots_francais()
    for i in range(len(liste_mots)):
        if str.count(liste_mots[i],caractere) == nombre:
            print(liste_mots[i])
    return None


def hamming(mot1, mot2):
    if len(mot1)!=len(mot2):
        return -1
    else:
        distance = 0
        for i in range(len(mot1)):
            if mot1[i]!=mot2[i]:
                distance +=1
        return distance


def indice_2eme_occurrence(chaine, caractere):
    ind = chaine.find(caractere)
    print("indice de la premiere occurrence :{}".format(ind))

    if ind == -1:
        return -1
    else:
        ind = chaine.find(caractere,ind+1)
        return ind


def scrabble(mot, lettres_disponibles):
    chaine_test = ""
    for i in range(len(mot)):
        if chaine_test.count(mot[i])==0:
            chaine_test+=mot[i]
            if mot.count(mot[i])>lettres_disponibles.count(mot[i]):
                return False
    return True


def suppression(mot, caractere):
    ind = mot.find(caractere)
    if ind == -1:
        return mot
    else:
        mot_mod = ""
        l = len(mot)
        for i in range(l):
            if i != ind:
                mot_mod += mot[i]
    return mot_mod


# Programme principal
def main():

    #affiche_debut_dictionnaire()
    #print(compte_mots_dictionnaire('w'))
    #affiche_mots_avec_caractere('z', 3)
    #print(hamming("test","beast"))
    #chaine = "Mon prix sera le votre"
    #caractere = 'o'

    #print("indice de la deuxieme occurrence :{}".format(indice_2eme_occurrence(chaine, caractere)))
    mot = "debutant"
    lettres_disponibles = "abctdegtnutttt"
    print("peut on écrire {} avec {} : {}".format(mot, lettres_disponibles, scrabble(mot, lettres_disponibles)))

    caractere = 't'
    print(suppression(mot,caractere))
if __name__ == '__main__':
    main()
# Fin
