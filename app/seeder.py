
from pymongo import MongoClient

from constantes import *


client = MongoClient(connect)
Magasin = client[db]
burgers= Magasin[collection]

b1 = { "prix" : 10, "description" : 'Burger1' , "allergènes" : ["moutarde"] , "cuisson" : "saignant", "scoville": 5000}
b2 = { "prix" : 15, "description" : 'Burger2' , "allergènes" : ["citron","noix"] , "cuisson" : "cuit", "scoville": 50000}
b3 = { "prix" : 19, "description" : 'Burger3' , "allergènes" : ["cacao","noix"] , "cuisson" : "à point", "scoville": 15000}



peuple_burgers = [b1,b2,b3]

burgers.insert_many(peuple_burgers)
