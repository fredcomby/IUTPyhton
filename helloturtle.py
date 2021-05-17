# coding: UTF-8
"""
Script: td_sphinx/helloturtle
Création: cleob, le 16/10/2019
"""
# Imports
import turtleiut as turtle  # import du module turtleiut en le faisant passer pour turtle


# Tracé
def un_trace():
    """Trace un dessin avec turtle
    """
    # Tracé d'un dessin
    turtle.up()  # Lève le pointeur
    turtle.goto(30, -10)  # Déplace le pointeur au point de coordonnées (30, -10)
    turtle.down()  # Abaisse le pointeur pour dessiner
    turtle.forward(100)  # Trace une ligne droite de longueur 100
    turtle.left(90)  # Tourne le pointeur à gauche de 90 degrés
    turtle.circle(100, 180)  # Trace un demi-cercle de rayon 100
    # en faisant tourner le pointeur dans le sens anti-horaire
    turtle.begin_fill()  # Déclare le début d'une zone à colorer
    turtle.circle(-100, 180)  # Trace un second demi-cercle de rayon 100
    # en faisant tourner le pointeur dans le sens horaire
    turtle.end_fill()  # Marque la fin d'une zone à colorer
    # => la coloration s'opère sur la portion dessinée entre le begin_fill et le end_fill
    turtle.up()  # Lève le pointeur
    turtle.goto(0, 0)  # replace le pointeur au point de coordonnées (0,0)
    return None


def main():
    # Initialisations de la fenetre turtle
    turtle.clear()  # créé une fenêtre vide
    turtle.Screen().setup(800, 600)  # retaille la fenêtre en 800 x 600 pixels
    turtle.shape('turtle')  # modifie de la forme du pointeur
    turtle.color("red")  # change la couleur de dessin en rouge

    un_trace()

    # Finalisation du script
    turtle.exitonclick()  # laisse la fenêtre visible jusqu'à ce que l'on clique dessus


if __name__ == '__main__':
    main()
# Fin
