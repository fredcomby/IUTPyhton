# coding: UTF-8
"""
Script: Prog_Pyhton/TP3/reglement.py
Création: frederic, le 16/03/2021
"""


# Imports

# Fonctions
def passage(note):
    if note <= 4:
        res = "éliminatoire"
    elif note < 8:
        res = "recalé"
    elif note < 10:
        res = "à rattraper"
    else:
        res = "validé"
    return res


# Programme principal
def main():
    res = passage(2)
    print(res)
    res = passage(4)
    print(res)
    res = passage(5)
    print(res)
    res = passage(8)
    print(res)
    res = passage(10)
    print(res)
    res = passage(19)
    print(res)


if __name__ == '__main__':
    main()
# Fin
