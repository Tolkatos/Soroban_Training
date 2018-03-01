import random
import count_error as ce

class LauncherText:
    def __init__(self):
        pass

    def check_rep(self, rep, total):
        correct = total
        if rep == correct:
            print("Bien joué !")
            print("Réponse : ", correct)
            return False
        else:
            print("Dommage !")
            print("Réponse : ", correct)
            return True

    def random_nbr(self, nbr):
        total = 0
        for nombre in range(nbr):
            nombre = random.randint(valeur_min, valeur_max)
            total += nombre
            print(nombre)
        return total

if __name__ == '__main__' :
    print("Nombre de répétitions ?")
    nbr_rep = int(input())
    print("Combien de nombre ?")
    nbr = int(input())
    print("Valeur min ?")
    valeur_min = int(input())
    print("Valeur max ?")
    valeur_max = int(input())
    error = ce.CountError()
    soroban = LauncherText()
    total = 0
    for play in range(nbr_rep):
        total = soroban.random_nbr(nbr)
        rep = int(input())
        error.is_correct(soroban.check_rep(rep, total))
        nbr_rep -= 1
        print("Nombre de répétitions restantes : ", nbr_rep)
    print("Nombre total d'erreur : ", error.nbr_error)

#Introduire choix addition/soustraction/multiplication
