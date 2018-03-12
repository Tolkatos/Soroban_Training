import random

class Calcul:
    def __init__(self):
        pass

    def addition(self, nbr, valeur_min, valeur_max):
        total = 0
        for nombre in range(nbr):
            nombre = random.randint(valeur_min, valeur_max)
            total += nombre
            print(nombre)
        return total

    def soustraction(self, nbr, valeur_min, valeur_max):
        total = 0
        for nombre in range(nbr):
            nombre = random.randint(valeur_min, valeur_max)
            total -= nombre
            print(nombre)
        return total

    def multiplication(self, nbr, valeur_min, valeur_max):
        total = 1
        for nombre in range(nbr):
            nombre = random.randint(valeur_min, valeur_max)
            total *= nombre
            print(nombre)
        return total
