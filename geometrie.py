# coding: UTF-8
"""
Script: Prog_Python/geometrie.py
Création: frederic, le 19/03/2021
"""


# Imports

# Fonctions
def carre(nb):
    for i in range(nb):
        print("*"*nb)
    return None


def triangle(nb):
    for i in range(nb):
        print("*"*(i+1))
    return None


def rectangle(largeur, hauteur):
    if (largeur < 2) | (hauteur < 2):
        return None
    else:
        print("+"+"-"*(largeur-2)+"+")
        for i in range(hauteur-2):
            print("|"+" "*(largeur-2)+"|")
        print("+"+"-"*(largeur-2)+"+")
    return None


def losange(nb):
    for i in range(nb):
        print(" "*(nb-i-1)+"/"+" "*2*i+"\\")
    for i in range(nb):
        print(" "*(i)+"\\"+" "*2*(nb-i-1)+"/")
    return None


def croix(x, y, taille):
    for i in range(taille):
        if i==(y-1):
            print("-"*(x-1)+"+"+"-"*(taille-x))
        else:
            print(" "*(x-1)+"|"+" "*(taille-x))
    return None

# Programme principal
def main():
    #print("Ho"*3 + "!"*5)
    carre(4)
    triangle(8)
    rectangle(3, 5)
    losange(4)
    croix(3, 2, 6)

if __name__ == '__main__':
    main()
# Fin
