import count_error as ce
import calcul as ca

class LauncherText:
    def __init__(self):
        self.error = ce.CountError()
        self.calcul = ca.Calcul()
        self.total = 0

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


if __name__ == '__main__' :
    print("Addition (A) / Soustraction (S) / Multiplication (M) ?")
    type_calcul = str(input())
    print("Nombre de répétitions ?")
    nbr_rep = int(input())
    print("Combien de nombre ?")
    nbr = int(input())
    print("Valeur min ?")
    valeur_min = int(input())
    print("Valeur max ?")
    valeur_max = int(input())
    soroban = LauncherText()
    for play in range(nbr_rep):
        if type_calcul == "A":
            soroban.total = soroban.calcul.addition(nbr, valeur_min, valeur_max)
        elif type_calcul == "S":
            soroban.total = soroban.calcul.soustraction(nbr, valeur_min, valeur_max)
        elif type_calcul == "M":
            soroban.total = soroban.calcul.multiplication(nbr, valeur_min, valeur_max)
        rep = int(input())
        soroban.error.is_correct(soroban.check_rep(rep, soroban.total))
        nbr_rep -= 1
        print("Nombre de répétitions restantes : ", nbr_rep)
    print("Nombre total d'erreur : ", soroban.error.nbr_error)

#Introduire choix addition/soustraction/multiplication
