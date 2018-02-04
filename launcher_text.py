import random

class LauncherText:
    def __init__(self, valeur_min, valeur_max):
        self.nbr_1 = random.randint(valeur_min, valeur_max)
        self.nbr_2 = random.randint(valeur_min, valeur_max)

    def check_rep(self, rep):
        correct = self.nbr_1 + self.nbr_2
        if rep == correct:
            print("Bien joué !")
            print("Réponse : ", correct)
        else:
            print("Dommage !")
            print("Réponse : ", correct)

if __name__ == '__main__' :
    print("Nombre de répétitions ?")
    nbr_rep = int(input())
    print("Valeur min ?")
    valeur_min = int(input())
    print("Valeur max ?")
    valeur_max = int(input())
    for play in range(nbr_rep):
        soroban = LauncherText(valeur_min, valeur_max)
        print(soroban.nbr_1)
        print(soroban.nbr_2)
        rep = int(input())
        soroban.check_rep(rep)
