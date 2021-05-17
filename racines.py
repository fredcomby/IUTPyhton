# coding: UTF-8
"""
Script: Prog_Pyhton/TP3/racines.py
Création: frederic, le 16/03/2021
"""


# Imports
import math


# Fonctions
def calcule_racines(a, b, c):
    if (a == 0) & (b == 0):
        return None
    elif a == 0:
        x_0 = -float(c/b)
        return x_0
    else:
        delta = b*b - 4*a*c
        if delta < 0:
            return None
        elif delta == 0:
            x_0 = -b/(2*a)
            return x_0
        else:
            x_1 = (-b-math.sqrt(delta))/(2*a)
            x_2 = (-b+math.sqrt(delta))/(2*a)
            return [x_1, x_2]


# Programme principal
def main():
    res = calcule_racines(2,-3,0)
    print(res)

if __name__ == '__main__':
    main()
# Fin
