# coding: UTF-8
"""
Script: Prog_Python/pascal.py
Création: frederic, le 22/03/2021
"""


# Imports
import math


# Fonctions
def triangle(N):
    for i in range(N+1):
        chaine = ""
        for j in range(i+1):
            chaine += str(j) + "\t"
        print(chaine)
    return None


def triangle_inverse(N):
    for i in range(N,-1,-1):
        chaine = ""
        for j in range(i+1):
            chaine += str(j) + "\t"
        print(chaine)
    return None


def triangle_pascal(N):
    for n in range(N,-1,-1):
        chaine = ""
        for p in range(n+1):
            c_n_p = int(math.factorial(n)/(math.factorial(p)*math.factorial(n-p)))
            chaine += str(c_n_p) + "\t"
        print(chaine)
    return None


# Programme principal
def main():
    triangle(6)
    triangle_inverse(6)
    triangle_pascal(6)

if __name__ == '__main__':
    main()
# Fin
