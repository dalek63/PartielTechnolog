from pydantic import BaseModel, validator


class Burger(BaseModel):
    prix : float
    description : str
    allergènes : list[str]
    cuisson : str 
    scoville : int 

    @validator("prix")
    def prix_is_valid(cls, v):
        if(v<10 or v>20):
            raise ValueError('Prix invalide')
        return v 
    
    @validator("allergènes")
    def allergènes_is_valid(cls, v):
        if ("crustacé" in v or "poisson" in v or "soja" in v or "céleri" in v or "mollusques" in v):
            raise ValueError('Allergènes invalides')
        return v

    @validator("cuisson")
    def cuisson_is_valid(cls,v):
        if (v not in ["saignant", "à point", "cuit"]):
            raise ValueError('Cuisson Invalide')
        return v

    @validator("scoville")
    def scoville_is_valid(cls,v):
        if (v%1000 != 0 or v<5000 or v>65000):
            raise ValueError('Indice Scoville invalide')
        return v 



# VARIABLE DE DEBUGAGE    
'''
b1 = Burger(prix = 10, description = 'Burger', allergènes = ['moutarde'], cuisson = 'saignant', scoville = 5000)

b2 = Burger(prix = 15, description = 'Burger', allergènes = ['citron'], cuisson = 'cuit', scoville = 30000)'''