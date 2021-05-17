# coding: UTF-8
"""
Script: Prog_Python/transmission.py
Création: frederic, le 06/04/2021
"""

# Imports
import tools_transmission
import random
import math
import numpy
import matplotlib.pyplot


# Fonctions
def saisie():
    cond = True
    chaine = ""
    while cond:
        print("saisissez une chaine d'au moins 10 caractères")
        chaine = input()
        if len(chaine) == 0:
            chaine = "j aime python"
            cond = False
        elif len(chaine) >= 10:
            cond = False
    return chaine


def codage_chaine2bits(message):
    code = []
    for i in range(len(message)):
        code.extend(tools_transmission.codage_caractere2bits(message[i]))
    return code


def decodage_bits2chaine(bits):
    chaine = ""
    for i in range(0, len(bits), 8):
        tranche = bits[i:i + 8]
        chaine += tools_transmission.decodage_bits2caractere(tranche)
    return chaine


def modulation(bits, A):
    signal_module = []
    for bit in bits:
        if bit == 0:
            signal_module += [-A]
        else:
            signal_module += [A]
    return signal_module


def canal(signal_module, P):
    signal_bruite = []
    for signal in signal_module:
        signal_bruite += [signal + random.gauss(0, math.sqrt(P))]
    return signal_bruite


def demodulation(signal_recu):
    signal_demodule = []
    for signal in signal_recu:
        if signal >= 0:
            signal_demodule += [1]
        else:
            signal_demodule += [0]
    return signal_demodule


def taux_erreur_binaire(bits_emis, bits_recus):
    taille = len(bits_emis)
    erreur = 0
    for i in range(taille):
        if bits_emis[i] != bits_recus[i]:
            erreur += 1
    return erreur / (taille)


# Programme principal
def main():
    A = 1
    # P = 2 * 10 ** (-1)
    # message = saisie()  # éventuellement "j aime python"
    # print("Message émis :", message)
    # bits_emis = codage_chaine2bits(message)
    # signal_module = modulation(bits_emis, A)
    # signal_bruite = canal(signal_module, P)
    # bits_recus = demodulation(signal_bruite)
    # message_recu = decodage_bits2chaine(bits_recus)
    # print("Message reçu :", message_recu)
    # Tracé avec matplotlib
    # tools_transmission.visualise_transmission(message, bits_emis, signal_module,
    #                                          signal_bruite, bits_recus, message_recu)

    # génération de la chaine aléatoire
    bits = []
    for i in range(1000):
        bits += [random.randint(0, 1)]

    signal_module = modulation(bits, A)
    liste_taux = []
    P = [p for p in numpy.arange(0.0, 1.01, 0.01)]
    for p in P:
        taux_local = 0
        for i in range(10):
            signal_bruite = canal(signal_module, p)
            signal_demodule = demodulation(signal_bruite)
            taux_local += taux_erreur_binaire(bits, signal_demodule)
        taux_local /=10 #valeur moyenne pour 10 bruitages différents
        liste_taux += [taux_local]

    matplotlib.pyplot.figure()  # Crée une nouvelle figure pyplot
    matplotlib.pyplot.semilogy(P, liste_taux, 'r.-')  # Trace la liste_sinc en fonction de la liste_angles en bleu
    matplotlib.pyplot.xlabel('Puissance')  # Définit la légende de l'axe des abscisses
    matplotlib.pyplot.ylabel('TEB')  # Définit la légende de l'axe des ordonnées
    matplotlib.pyplot.legend(["Taux d'erreur en fonction de la puissance de bruit"])  # Définit la légende des courbes
    matplotlib.pyplot.grid(True)  # Ajoute une grille
    matplotlib.pyplot.show()  # Affiche les tracés


if __name__ == '__main__':
    main()
# Fin
