# coding: UTF-8
"""
Script: Prog_Python/syracuse.py
Création: frederic, le 22/03/2021
"""


# Imports

N_MAX = 25     # nombre de termes maximum dans l'analyse des suites de Syracuse

# Fonctions
def prochaine_valeur(u_n):
    if (u_n % 2) == 0:
        u_np1 = u_n//2
    else:
        u_np1 = 3*u_n + 1
    return u_np1

def vol(a, N):
    val = a
    chaine = "{}".format(a)
    for i in range(N):
        val = prochaine_valeur(val)
        chaine += ", {}".format(val)
    print(chaine)


def temps_vol(a):
    val = a
    temps = 0
    for i in range(N_MAX):
        if val == 1:
            return temps
        else:
            val = prochaine_valeur(val)
            temps +=1
    return N_MAX


def altitude_max(a):
    temps = temps_vol(a)
    val = a
    val_max = a
    for i in range(temps):
        val = prochaine_valeur(val)
        if val > val_max:
            val_max = val
    return val_max


# Programme principal
def main():
    vol(14,17)


if __name__ == '__main__':
    main()
# Fin
