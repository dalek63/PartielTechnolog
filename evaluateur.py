from burgers import * 


class EvaluateurVentes:
    def __init__(self, date):
        self.date = date
        self.burgers = []

    
    def ajout_burger(self, b):
        self.burgers.append(b)
    

    def évaluer(self):
        res = len(self.burgers)
        return res

    def prix_total(self):
        res = 0
        for i in range(len(self.burgers)):
            res = res + self.burgers[i].prix
        return res    