# coding: UTF-8
"""
Script: Prog_Python/crypto.py
Création: frederic, le 30/03/2021
"""

# Imports
import string


# Fonctions
def car_rot13(car):
    alphabet = string.ascii_lowercase
    car_out = alphabet[(alphabet.find(car) + 13) % 26]
    return car_out


def rot13(chaine):
    chaine_out = ""
    for i in range(len(chaine)):
        chaine_out += car_rot13(chaine[i])
    return chaine_out


def car_cesar(car, nombre):
    alphabet = string.ascii_lowercase
    return alphabet[(alphabet.find(car) + nombre) % 26]


def vigenere_numerique(chaine, liste):
    chaine_out = ""
    for i in range(len(chaine)):
        chaine_out += car_cesar(chaine[i], liste[i % len(liste)])
    return chaine_out


def erenegiv_numerique(chaine, liste):
    chaine_out = ""
    for i in range(len(chaine)):
        chaine_out += car_cesar(chaine[i], -liste[i % len(liste)])
    return chaine_out


def vigenere(chaine,clef):
    chaine_out = ""
    for i in range(len(chaine)):
        chaine_out += car_cesar(chaine[i], ord(clef[i % len(clef)])-ord('a'))
    return chaine_out


def erenegiv(chaine, clef):
    chaine_out = ""
    for i in range(len(chaine)):
        chaine_out += car_cesar(chaine[i], -ord(clef[i % len(clef)])+ord('a'))
    return chaine_out

# Programme principal
def main():
    car = 'n'
    print(car_rot13(car))
    chaine = "abracadabra"
    print(rot13(chaine))
    chaine = "nostradamus"
    print(rot13(chaine))
    print(car_cesar('a', 2))
    chaine = "abracadabra"
    liste = [1, 2, 3, 4]
    print(vigenere_numerique(chaine, liste))
    chaine = "lutxwidpvovaxacpgn"
    liste = [2, 0, 1, 7]
    print(erenegiv_numerique(chaine, liste))
    chaine = "jusquicitoutvabien"
    liste = "python"
    print(vigenere(chaine, liste))
    chaine = "yslxivrgmvigkyupsa"
    liste = "python"
    print(erenegiv(chaine, liste))

if __name__ == '__main__':
    main()
# Fin
