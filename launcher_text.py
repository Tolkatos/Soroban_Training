import random
import count_error as ce

class LauncherText:
    def __init__(self, valeur_min, valeur_max):
        self.nbr_1 = random.randint(valeur_min, valeur_max)
        self.nbr_2 = random.randint(valeur_min, valeur_max)

    def check_rep(self, rep):
        correct = self.nbr_1 + self.nbr_2
        if rep == correct:
            print("Bien joué !")
            print("Réponse : ", correct)
            return False
        else:
            print("Dommage !")
            print("Réponse : ", correct)
            return True

if __name__ == '__main__' :
    print("Nombre de répétitions ?")
    nbr_rep = int(input())
    print("Valeur min ?")
    valeur_min = int(input())
    print("Valeur max ?")
    valeur_max = int(input())
    error = ce.CountError()
    for play in range(nbr_rep):
        soroban = LauncherText(valeur_min, valeur_max)
        print(soroban.nbr_1)
        print(soroban.nbr_2)
        rep = int(input())
        error.is_correct(soroban.check_rep(rep))
        nbr_rep -= 1
        print("Nombre de répétitions restantes : ", nbr_rep)
    print("Nombre total d'erreur : ", error.nbr_error)

#Introduire choix du nombre de Nombre
#Introduire choix addition/soustraction/multiplication
