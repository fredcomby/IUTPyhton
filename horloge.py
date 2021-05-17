# coding: UTF-8
"""
Script: Prog_Pyhton/horloge.py
Création: frederic, le 17/03/2021
"""


# Imports
import tools_horloge


# Fonctions
def calcule_offset_horloge(offset):
    heures = tools_horloge.get_heures()
    minutes = tools_horloge.get_minutes()
    minutes += offset
    new_minutes = minutes % 60
    new_heures = (heures + minutes // 60)%24
    tools_horloge.affiche_heure(new_heures,new_minutes)
    return [new_heures , new_minutes]

# Programme principal
def main():
    print(tools_horloge.get_heures())
    print(tools_horloge.get_minutes())

    calcule_offset_horloge(70)

if __name__ == '__main__':
    main()
# Fin
