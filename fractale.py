# coding: UTF-8
"""
Script: Prog_Python/fractale.py
Création: frederic, le 23/03/2021
"""


# Imports
import turtleiut as turtle

# Fonctions
def triangle(l):
    for i in range(3):
        turtle.down()
        turtle.forward(l)
        turtle.left(120)
        turtle.up()


def motif1(l):
    turtle.down()
    turtle.forward(l / 3)
    turtle.right(60)
    turtle.forward(l / 3)
    turtle.left(120)
    turtle.forward(l / 3)
    turtle.right(60)
    turtle.forward(l / 3)
    turtle.up()


def motif2(l):
    motif1(l/3)
    turtle.right(60)
    motif1(l / 3)
    turtle.left(120)
    motif1(l / 3)
    turtle.right(60)
    motif1(l / 3)


def motif3(l):
    motif2(l/3)
    turtle.right(60)
    motif2(l / 3)
    turtle.left(120)
    motif2(l / 3)
    turtle.right(60)
    motif2(l / 3)


def flocon1():
    longueur = 100
    for i in range(3):
        motif1(longueur)
        turtle.left(120)


def flocon2():
    longueur = 200
    for i in range(3):
        motif2(longueur)
        turtle.left(120)


def flocon3(longueur):
    for i in range(3):
        motif3(longueur)
        turtle.left(120)

def flocon(longueur, ordre):
    for i in range(3):
        motif(longueur, ordre)
        turtle.left(120)


def motif(longueur, ordre=1):
    if ordre <=0:
        turtle.down()
        turtle.forward(longueur)
        turtle.up()
    else:
        turtle.down()
        motif(longueur/3,ordre-1)
        turtle.right(60)
        motif(longueur/3,ordre-1)
        turtle.left(120)
        motif(longueur/3,ordre-1)
        turtle.right(60)
        motif(longueur/3,ordre-1)
        turtle.up()


# Programme principal
def main():
    turtle.clear()  # créé une fenêtre vide
    turtle.Screen().setup(1000, 800)  # retaille la fenêtre en 800 x 600 pixels
    turtle.shape('classic')  # modifie de la forme du pointeur
    turtle.up()
    turtle.goto(-200,-200)
    turtle.down()

    #triangle(70)
    #motif1(70)
    #flocon1()
    #motif2(100)
    #flocon2()
    #flocon3(200)
    #motif(200,3)
    flocon(400,3)

    turtle.exitonclick()  # laisse la fenêtre visible jusqu'à ce que l'on clique dessus
if __name__ == '__main__':
    main()
# Fin
