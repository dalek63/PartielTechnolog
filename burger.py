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


b = Burger(prix = 10, description = 'Burger', allergènes = ['moutarde'], cuisson = 'saignant', scoville = 5)

