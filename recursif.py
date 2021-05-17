# coding: UTF-8
"""
Script: Prog_Python/recursif.py
Création: frederic, le 23/03/2021
"""


# Imports

# Fonctions
def heron(a, b, n):
    if n==0:
        return a
    else:
        return heron(a, b, n - 1) / 2 + b / heron(a, b, n - 1)


def somme_riemann(n):
    if n==1:
        return 1
    else:
        return somme_riemann(n-1) + 1/(n*n)


def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

# Programme principal
def main():
    pass


if __name__ == '__main__':
    main()
# Fin
