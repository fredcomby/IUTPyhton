# coding: UTF-8
"""
Script: Prog_Python/carre.py
Création: frederic, le 22/03/2021
"""


# Imports

# Fonctions
def carre2D():
    for dizaine in range (10):
        chaine = ""
        for unite in range(10):
            chaine += str(dizaine)+str(unite)+" "
        print(chaine)
    return None


def carre2D_barre(dizaine, unite):
    for diz in range (10):
        chaine = ""
        for uni in range(10):
            if (diz == dizaine) | (uni == unite):
                chaine += "**" + " "
            else:
                chaine += str(diz) + str(uni) + " "
        print(chaine)
    return None


def multiplication():
    for lin in range (10):
        chaine = ""
        for col in range(10):
            chaine += str((lin+1)*(col+1)) + "\t"
        print(chaine)
    return None



# Programme principal
def main():
    carre2D()
    carre2D_barre(6,3)
    multiplication()

if __name__ == '__main__':
    main()
# Fin
