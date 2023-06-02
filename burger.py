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
    



#b = Burger(prix = 10, description = 'Burger', allergènes = ['moutarde'], cuisson = 'saignant', scoville = 5)

