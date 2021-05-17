# coding: UTF-8
"""
Script: Prog_Python/estimation.py
Création: frederic, le 22/03/2021
"""

# Imports
import math
import random
import turtleiut as turtle


# Fonctions
def riemann(n):
    S = 0
    if n <= 0:
        return None

    for i in range(n):
        S += 1 / (math.pow(i + 1, 2))
    return math.sqrt(6 * S)


def calcul_erreur_relative(valeur):
    return round(100 * abs(valeur - math.pi) / math.pi, 3)


def convergence_riemann():
    for i in range(6):
        ind = int(math.pow(10,i+1))
        valeur = riemann(ind)
        print("estimation pour n={} : {} ({}% d'erreur)".format(ind, valeur, calcul_erreur_relative(valeur)))
    return None


def est_dans_cercle(x, y):
    if math.sqrt(x * x + y * y) <= 1:
        return True
    else:
        return False


def monte_carlo(n):
    trace = False
    if trace:
        # on multiplie tout par 100 pour bien voir
        turtle.clear()  # créé une fenêtre vide
        turtle.Screen().setup(800, 600)  # retaille la fenêtre en 800 x 600 pixels
        turtle.shape('classic')  # modifie de la forme du pointeur
        turtle.up()  # Lève le pointeur
        turtle.home()
        turtle.down()  # Abaisse le pointeur pour dessiner
        turtle.color("grey")  # change la couleur de dessin en rouge
        turtle.forward(100)  # Trace une ligne droite de longueur 100
        turtle.begin_fill()  # Déclare le début d'une zone à colorer
        turtle.left(90)  # Tourne le pointeur à gauche de 90 degrés
        turtle.circle(100, 90)  # Trace un quart de cercle de rayon 100
        turtle.left(90)
        turtle.forward(100)
        turtle.end_fill()  # Marque la fin d'une zone à colorer
        turtle.color("black")  # change la couleur de dessin en rouge
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.circle(100, 450)
        turtle.left(90)
        turtle.forward(100)
        turtle.up()
    C = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if est_dans_cercle(x, y):
            if trace:
                turtle.goto(100 * x, 100 * y)
                turtle.color("red")
                turtle.dot(4,"red")
            C += 1
        else:
            if trace:
                turtle.goto(100 * x, 100 * y)
                turtle.dot(4,"blue")
    return 4 * C / n


def convergence_monte_carlo():
    for i in range(6):
        ind = int(math.pow(10,i+1))
        valeur = monte_carlo(ind)
        print("estimation pour n={} : {} ({}% d'erreur)".format(ind, valeur, calcul_erreur_relative(valeur)))
    return None


# Programme principal
def main():
    print("riemann de 200: {}".format(riemann(6)))
    print("erreur en %: {}".format(calcul_erreur_relative(riemann(6))))
    convergence_riemann()
    convergence_monte_carlo()


if __name__ == '__main__':
    main()
# Fin
