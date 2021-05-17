# coding: UTF-8
"""
Script: Prog_Python/parfait.py
Création: frederic, le 06/04/2021
"""


# Imports

# Fonctions
def diviseurs(n):
    diviseurs = []
    if n == 0:
        print("le nombre doit être non nul")
        return False

    for i in range(1,n+1):
        if n%i == 0:
            diviseurs += [i]
    return diviseurs


def est_parfait(n):
    if n==0:
        print("le nombre doit être non nul")
        return False
    liste_diviseurs = diviseurs(n)
    somme = 0
    for div in liste_diviseurs:
        somme += div
    if somme == 2*n:
        return True
    else:
        return False

def calcul_liste_entiers_parfaits(N):
    liste_entiers_parfaits = []
    for i in range(1,N+1):
        if est_parfait(i):
            liste_entiers_parfaits += [i]
    return liste_entiers_parfaits


# Programme principal
def main():
    print(calcul_liste_entiers_parfaits(1000))

if __name__ == '__main__':
    main()
# Fin
