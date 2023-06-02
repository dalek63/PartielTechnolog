from burger import * 
import unittest
from mock import Mock

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

    def total_allergènes(self):
        res = []
        for i in range(len(self.burgers)):
            res.extend(self.burgers[i].allergènes)
        return res


#TESTS

class TestEvaluateur(unittest.TestCase):
    def setUp(self):
        musique = Mock()
        self.evaluateur = EvaluateurVentes(
            date = "10/10/2010",
        )

    # Test  ajouter burger  
    def test_add_burger(self):
        burger = Mock()
        self.evaluateur.ajout_burger()
        self.assertEqual(self.evaluateur.burgers , [burger])

#CLASSE DE DEBUGAGE
'''
e = EvaluateurVentes('10/10/2010')

e.ajout_burger(b1)
e.ajout_burger(b2)

print(e.prix_total())'''