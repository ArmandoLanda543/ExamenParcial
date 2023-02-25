
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class Continente(BaseModel):
    Code:str
    Nombre:str

list_Continente = [Continente(Code='ANT', Nombre='ANTARTICA'),
                    Continente(Code='AS', Nombre='ASIA'),
                     Continente(Code='EUR', Nombre='EUROPA'),
                     Continente(Code='AFR', Nombre='AFRICA'),
                     Continente(Code='NOR', Nombre='NORTE AMERICA'),
                     Continente(Code='OCE', Nombre='OCEANIA'),
                     Continente(Code='SOU', Nombre='SUR AMERICA')]


#################################################### GET ########################################################################

@router.get("/ExamenParcial/A/{Continente2}",status_code=200)
async def get_Continente(Continente2:str):
    if Continente2 == 'continente':
        return list_Continente
    else:
        raise HTTPException(status_code=400, detail="URL Incorrecta, intentelo de nuevo")
    

#################################################### POST ########################################################################
@router.post("/ExamenParcial/A/{Continente2}",status_code=201)
async def post_Continente(Continente2:str,continente:Continente):
    found=False
    if Continente2 == 'continente':

        for index, save_continente in enumerate(list_Continente):
            if save_continente.Code == continente.Code:
                raise HTTPException(status_code=400, detail="El continente ya existe")
        else:
            list_Continente.append(continente)
            raise HTTPException(status_code=201, detail="Continente creado exitosamente")
        
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    
#################################################### PUT ########################################################################
@router.put("/ExamenParcial/A/{Continente2}",status_code=201)
async def put_Continente(Continente2:str,continente:Continente):
    found=False

    if Continente2 == 'continente':
        for index, save_continente in enumerate(list_Continente):
            if save_continente.Code == continente.Code:
                list_Continente[index] = continente
                found=True
        if not found:
            raise HTTPException(status_code=404, detail="Continente No Existe")
        else:
            raise HTTPException(status_code=200, detail="El continente Fue Actualizado Exitosamente")
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    

#################################################### DELETE ########################################################################
@router.delete("/ExamenParcial/A/{Continente2}/{Code}")
async def delete_Continente(Continente2:str,Code:str):
    found=False

    if Continente2 == 'continente':

        for index, saved_continente in enumerate(list_Continente):
            if saved_continente.Code == Code:  #
                del list_Continente[index]  
                found=True
                raise HTTPException(status_code=200, detail="El continente Fue Eliminado Exitosamente")
        
        if not found:
            raise HTTPException(status_code=204, detail="Continente No Existe")
        
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    
        
