# coding: UTF-8
"""
Script: Prog_Python/scodoc.py
Création: frederic, le 09/04/2021
"""


# Imports
import pprint

# Fonctions
def creation_etudiant(nom, genre, identifiant):
    etudiant = {
        'nom' : nom,
        'genre' : genre,
        'identifiant' : identifiant,
    }
    return etudiant


# Programme principal
def main():
    etu = creation_etudiant("Barbara", "F", "ETUD001")
    pprint.pprint()

if __name__ == '__main__':
    main()
# Fin
