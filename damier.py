# coding: UTF-8
"""
Script: Prog_Python/damier.py
Création: frederic, le 22/03/2021
"""


# Imports
import turtleiut as turtle  # import du module turtleiut en le faisant passer pour turtle

# Fonctions
def carre(x,y,cote,couleur):
    turtle.up()  # Lève le pointeur
    turtle.goto(x,y)  # Déplace le pointeur au point de coordonnées (x,y)
    turtle.down()  # Abaisse le pointeur pour dessiner
    turtle.color(couleur)  # change la couleur de dessin en rouge
    turtle.begin_fill()  # Déclare le début d'une zone à colorer
    for i in range(4):
        turtle.forward(cote)  # Trace une ligne droite de longueur 100
        turtle.right(90)  # Tourne le pointeur à gauche de 90 degrés
    turtle.end_fill()  # Marque la fin d'une zone à colorer
    turtle.up()  # Lève le pointeur
    return None

def ligne(x,y,taille,liste_couleur):
    for i in range(10):
        carre(x+i*taille,y,taille,liste_couleur[i%2])
    return None


def deux_lignes(x,y,taille,liste_couleur):
    for ligne in range(2):
        for i in range(10):
            carre(x+i*taille,y-ligne*taille,taille,liste_couleur[(i+ligne)%2])
    return None


def damier(x,y,taille,liste_couleur):
    for ligne in range(5):
        deux_lignes(x,y-ligne*2*taille, taille,liste_couleur)
    return None

# Programme principal
def main():
    turtle.tracer(20)
    # Initialisations de la fenetre turtle
    turtle.clear()  # créé une fenêtre vide
    turtle.Screen().setup(800, 600)  # retaille la fenêtre en 800 x 600 pixels
    turtle.shape('classic')  # modifie de la forme du pointeur

    carre(50,70,30,"blue")
    Liste_couleur = ["yellow", "blue"]
    ligne(-200, 200, 40, Liste_couleur)
    deux_lignes(-200, 200, 40, Liste_couleur)
    damier(-200, 200, 40, Liste_couleur)

    # Finalisation du script
    turtle.exitonclick()  # laisse la fenêtre visible jusqu'à ce que l'on clique dessus

if __name__ == '__main__':
    main()
# Fin
