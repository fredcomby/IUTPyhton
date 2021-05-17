# coding: UTF-8
"""
Script: Prog_Pyhton/TP2/convert.py
Création: frederic, le 16/03/2021
"""

# Imports
# import tools_tests
# import introspection

import tools_convert


# Fonctions
def celsius2fahrenheit(temperature):
    """ Convertit une température donnée en ° Celsius en ° Farenheit
    """
    res = 1.8 * temperature + 32
    return res


def celsius2kelvin(temperature):
    """ Convertit une température donnée en ° Celsius en Kelvin
    """
    res = temperature + 273.15
    return res


# Programme principal
def main():
    Ville = "Grenoble"
    T = tools_convert.get_temperature(Ville, False)
    print("La température à {} est de :".format(Ville))
    print("> {}°C".format(T))
    print("> ou de manière équivalente, {}°F et {}K.".format(celsius2fahrenheit(T), celsius2kelvin(T)))


if __name__ == '__main__':
    main()
# Fin
