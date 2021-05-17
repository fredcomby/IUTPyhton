# coding: UTF-8
"""
Script: Prog_Python/tournons.py
Création: frederic, le 06/04/2021
"""

# Imports
import matplotlib.pyplot
import numpy
import math


# Fonctions
def get_angles():
    angles = [i for i in numpy.arange(-1000, 1000.5, 0.5)]
    return angles


def degre_vers_radian(angle):
    return angle * math.pi / 180.0


def calcul_sinus_cardinal(angles):
    sinus_cardinal = []
    for angle in angles:
        angle_rad = degre_vers_radian(angle)
        if angle == 0:
            sinus_cardinal += [1]
        else:
            sinus_cardinal += [math.sin(angle_rad) / angle_rad]
    return sinus_cardinal


# Programme principal
def main():
    liste_angles = get_angles()  # Récupère la liste d'angles
    liste_sinc = calcul_sinus_cardinal(liste_angles)  # Calcule le sinus des angles

    # Affichage
    matplotlib.pyplot.figure()  # Crée une nouvelle figure pyplot
    matplotlib.pyplot.plot(liste_angles, liste_sinc, 'b-')  # Trace la liste_sinc en fonction de la liste_angles en bleu
    matplotlib.pyplot.xlabel('angle (en degré)')  # Définit la légende de l'axe des abscisses
    matplotlib.pyplot.ylabel('sinc(angle)')  # Définit la légende de l'axe des ordonnées
    matplotlib.pyplot.legend(['sinc(x)'])  # Définit la légende des courbes
    matplotlib.pyplot.grid(True)  # Ajoute une grille
    matplotlib.pyplot.show()  # Affiche les tracés


if __name__ == '__main__':
    main()
# Fin
