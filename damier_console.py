# coding: UTF-8
"""
Script: Prog_Python/damier_console.py
Création: frederic, le 22/03/2021
"""


# Imports

# Fonctions
def segment(cote, motif):
    print((motif + " ") * cote, end='')


def ligne(nb_segments, taille, motifs):
    for i in range(nb_segments):
        segment(taille, motifs[i % 2])
    print()


def rangee(nb_segments, taille, motifs):
    for i in range(taille):
        ligne(nb_segments, taille, motifs)


def damier(nb_carres, taille, motifs):
    for i in range(nb_carres):
        if i % 2 == 0:
            rangee(nb_carres, taille, [motifs[0], motifs[1]])
        else:
            rangee(nb_carres, taille, [motifs[1], motifs[0]])


# Programme principal
def main():
    segment(4, "o")
    print()
    ligne(5, 5, ['o', 'x'])
    print()
    rangee(5, 3, ['x', '#'])
    print()
    damier(5, 3, ['♡', '.'])


if __name__ == '__main__':
    main()
# Fin
