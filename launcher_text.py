import count_error as ce
import calcul as ca
import backups_files as bf

class LauncherText:
    def __init__(self):
        self.error = ce.CountError()
        self.calcul = ca.Calcul()
        self.total = 0
        self.data = bf.Files()

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

    def run(self, type_calcul, nbr_rep, nbr, valeur_min, valeur_max):
        for play in range(nbr_rep):
            if type_calcul == "A":
                self.total = self.calcul.addition(nbr, valeur_min, valeur_max)
            elif type_calcul == "S":
                self.total = self.calcul.soustraction(nbr, valeur_min, valeur_max)
            elif type_calcul == "M":
                self.total = self.calcul.multiplication(nbr, valeur_min, valeur_max)
            rep = int(input())
            self.error.is_correct(self.check_rep(rep, self.total))
            nbr_rep -= 1
            print("Nombre de répétitions restantes : ", nbr_rep)
        print("Nombre total d'erreur : ", self.error.nbr_error)
        print("Partie précédente : ", self.data.load_data())
        self.data.save_data(str(soroban.error.nbr_error))

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
    soroban.run(type_calcul, nbr_rep, nbr, valeur_min, valeur_max)
