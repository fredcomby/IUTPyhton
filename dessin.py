# coding: UTF-8
"""
Script: Prog_Python/dessin.py
Création: frederic, le 19/03/2021
"""


# Imports
import turtleiut as turtle
# Fonctions
def carre(x, y, cote, couleur):
    # Tracé d'un carré
    turtle.color(couleur)  # change la couleur de dessin en rouge
    turtle.up()  # Lève le pointeur
    turtle.goto(x, y)  # Déplace le pointeur au point de coordonnées (x,y) coin haut gauche du carré)
    turtle.down()  # Abaisse le pointeur pour dessiner
    for i in range(4):
        turtle.forward(cote)  # Trace une ligne droite de longueur cote
        turtle.right(90)  # Tourne le pointeur à droite de 90 degrés
    turtle.up()  # Lève le pointeur
    turtle.goto(0, 0)  # replace le pointeur au point de coordonnées (0,0)
    return None


def spirale(x, y, nbre_segments, espacement, couleur):
    # Tracé d'une spirale carrée
    turtle.color(couleur)  # change la couleur de dessin en rouge
    turtle.up()  # Lève le pointeur
    turtle.goto(x, y)  # Déplace le pointeur au point de coordonnées (x,y) coin haut gauche du carré)
    turtle.down()  # Abaisse le pointeur pour dessiner
    for i in range(nbre_segments):
        turtle.forward((i+1)*espacement)  # Trace une ligne droite de longueur cote
        turtle.right(90)  # Tourne le pointeur à droite de 90 degrés
    turtle.up()  # Lève le pointeur
    turtle.goto(0, 0)  # replace le pointeur au point de coordonnées (0,0)
    return None


def pentacle(x, y, longueur, couleur):
    # Tracé d'un pentacle
    turtle.color(couleur)  # change la couleur de dessin en rouge
    turtle.up()  # Lève le pointeur
    turtle.goto(x, y)  # Déplace le pointeur au point de coordonnées (x,y) coin haut gauche du carré)
    turtle.down()  # Abaisse le pointeur pour dessiner
    for i in range(5):
        turtle.forward(longueur)  # Trace une ligne droite de longueur cote
        turtle.right(180 - 180/5)  # Tourne le pointeur à droite de 90 degrés
    turtle.up()  # Lève le pointeur
    turtle.goto(0, 0)  # replace le pointeur au point de coordonnées (0,0)
    return None


def rectangle(x1, y1, x2, y2, couleur, remplir):
    turtle.color(couleur)
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    if remplir:
        turtle.begin_fill()
    turtle.goto(x2,y1)
    turtle.goto(x2,y2)
    turtle.goto(x1,y2)
    turtle.goto(x1,y1)
    if remplir:
        turtle.end_fill()
    turtle.up()


# Programme principal
def main():
    turtle.clear()  # créé une fenêtre vide
    turtle.Screen().setup(800, 600)  # retaille la fenêtre en 800 x 600 pixels
    turtle.shape('turtle')  # modifie de la forme du pointeur

    # carre(10,20,40,"green")
    pentacle(0, 0, 100, "red")

    rectangle(10,10,150,200,'red',True)

    # Finalisation du script
    turtle.exitonclick()  # laisse la fenêtre visible jusqu'à ce que l'on clique dessus

if __name__ == '__main__':
    main()
# Fin
