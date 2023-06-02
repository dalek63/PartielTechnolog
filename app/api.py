from fastapi import FastAPI
from pymongo import MongoClient
from constantes import *
from burger import *
from evaluateur import * 
from bson.objectid import ObjectId


client = MongoClient(connect)
Magasin = client[db]
burgers= Magasin[collection1]
evaluateurs = Magasin[collection2]

app = FastAPI()


# Routes pour les Burgers


@app.get("/burgers")
async def get_burgers():
    res = []
    for i in burgers.find():
        res.append(Burger(**i))
    return res

@app.post("/burgers")
async def create_burger(burger : Burger):

    result = burgers.insert_one(dict(burger))
    
    return {"_id": str(result.inserted_id)} | dict(burger)


#Avoir tout les burgers infèrieurs  ou egaux au prix entré

@app.get("/burgers-prix/{prix}")
async def get_burgerByprice(prix: float):

    res = []
    for i in burgers.find({"prix": { "$lte": prix }}):
        res.append(Burger(**i))

    if res!=[]:
        return res
    else:
        return "Aucun burger n'est à ce prix"

#Avoir tout les burgers par cuisson 

@app.get("/burgers-cuisson/{cuisson}")
async def get_burgerBycuisson(cuisson: str):
    burger = burgers.find_one({"cuisson": cuisson})
    if burger:
        return Burger(**burger)
    else:
        return "Aucune cuisson à ce nom "

#Avoir les burgers inferieurs a l'unité de scoville entrée


@app.get("/burgers-scoville/{scoville}")
async def get_burgerBycuisson(scoville: int):
    
    res = []
    for i in burgers.find({"scoville": { "$lte" : scoville}}):
        res.append(Burger(**i))

    if res!=[]:
        return res
    else:
        return "Aucun Burger avec une unité de scoville aussi faible"


#TROUVER BURGER AVEC ALLERGENE 

@app.get("/burgers-allergenes/{allergene}")
async def get_burgerBycuisson(allergene: str):
    
    res = []
    for i in burgers.find({"allergènes" : allergene } ):
        res.append(Burger(**i))

    if res!=[]:
        return res
    else:
        return "Aucun Burger avec cette allergie"






#SUPPRIMER UN BURGER NECESSITE UNE IDEE ALORS j'AI MIS l'ID GENEREE PAR MONGODB EN PARAMETRE DONC IL FAUT ALLER LA CHERCHER DANS LA BASE

@app.delete("/burgers/{id}}")
def delete_burger(id: str):
    res = burgers.find_one({"_id": ObjectId(id)})

    if res :
        
        burgers.delete_one({"_id": ObjectId(id)})

        return {"message": "Burger supprimé"}

    else :

        return {"message": "Burger introuvable"}


    
