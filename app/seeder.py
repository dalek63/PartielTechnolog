
from pymongo import MongoClient

from constantes import *


client = MongoClient(connect)
Magasin = client[db]
burgers= Magasin[collection1]
evaluateurs = Magasin[collection2]

b1 = { "prix" : 10, "description" : 'Burger1' , "allergènes" : ["moutarde"] , "cuisson" : "saignant", "scoville": 5000}
b2 = { "prix" : 15, "description" : 'Burger2' , "allergènes" : ["citron","noix"] , "cuisson" : "cuit", "scoville": 50000}
b3 = { "prix" : 19, "description" : 'Burger3' , "allergènes" : ["cacao","noix"] , "cuisson" : "à point", "scoville": 15000}



peuple_burgers = [b1,b2,b3]

peuple_evaluateurs = [
    { "date" : "10/10/2010", "burgers" : [b1,b1,b2]},
    { "date" : "11/10/2010", "burgers" : [b1,b1,b2,b2]},
    { "date" : "12/10/2010", "burgers" : [b3,b3]}
]

burgers.insert_many(peuple_burgers)

evaluateurs.insert_many(peuple_evaluateurs)