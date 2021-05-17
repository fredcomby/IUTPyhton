# coding: UTF-8
"""
Script: Prog_Python/syracuse_graphique.py
Création: frederic, le 22/03/2021
"""


# Imports
import dessin
import turtleiut as turtle
import syracuse
import tools_couleurs

# Fonctions
def vol_graphique(a, couleur):

    affiche_valeur = True
    val = a
    dessin.rectangle(0, 0, 1, a, couleur, True)
    if affiche_valeur:
        #turtle.up()
        turtle.goto(0, a)
        turtle.color("red")
        turtle.write(str(a))
        turtle.color(couleur)
    for i in range(syracuse.N_MAX):
        val = syracuse.prochaine_valeur(val)
        dessin.rectangle(i+1,0,i+2,val,couleur,True)
        if affiche_valeur:
            #turtle.up()
            turtle.goto(i+1,val)
            turtle.color("red")
            turtle.write(str(val))
            turtle.color(couleur)


def vols_graphiques(a, b):
    for i in range(a,b,1):
        print(i)
        vol_graphique(i,tools_couleurs.COULEURS[i])




# Programme principal
def main():
    turtle.clear()  # créé une fenêtre vide
    turtle.Screen().setup(800, 600)  # retaille la fenêtre en 800 x 600 pixels
    turtle.shape('classic')  # modifie de la forme du pointeur

    #récupération d'info sur la suite
    # val_max = syracuse.altitude_max(17)
    # turtle.Screen().setworldcoordinates(-1, -1, syracuse.N_MAX + 2, val_max + 2)
    # vol_graphique(17,"blue")
    val_max = 0
    for i in range(13,25,1):
        val = syracuse.altitude_max(i)
        if val>val_max:
            val_max = val
    turtle.Screen().setworldcoordinates(-1, -1, syracuse.N_MAX + 2, val_max + 2)
    vols_graphiques(13,25)


    turtle.exitonclick()  # laisse la fenêtre visible jusqu'à ce que l'on clique dessus

if __name__ == '__main__':
    main()
# Fin
