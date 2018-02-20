class CountError:
    def __init__(self):
        self.nbr_error = 0

    def is_correct(self, resultat):
        if resultat:
            self.nbr_error +=1
