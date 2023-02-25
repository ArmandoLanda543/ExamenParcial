
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class ContinenteRegion(BaseModel):
    Code:str
    NomContinente:str
    NombreReg:str

list_Continente_Region = [ContinenteRegion(Code='ANT', NomContinente='Antartida', NombreReg='ANTARTIDA'),
                          
                    ContinenteRegion(Code='AUS',NomContinente='Oceania', NombreReg='AUSTRALIA Y NUEVA ZELANDA'),
                    ContinenteRegion(Code='MEL',NomContinente='Oceania', NombreReg='MELANESIA'),
                    ContinenteRegion(Code='MIC',NomContinente='Oceania', NombreReg='MICRONESIA'),
                    ContinenteRegion(Code='POL',NomContinente='Oceania', NombreReg='POLINESIA'),

                     ContinenteRegion(Code='EUR',NomContinente='Europa', NombreReg='BALTICO'),
                        ContinenteRegion(Code='BRI',NomContinente='Europa', NombreReg='BRITANICO'),
                        ContinenteRegion(Code='EDE',NomContinente='Europa', NombreReg='ESTE DE EUROPA'),
                        ContinenteRegion(Code='NOR',NomContinente='Europa', NombreReg='NORDICO'),
                        ContinenteRegion(Code='EDS',NomContinente='Europa', NombreReg='EUROPA DEL SUR'),
                        ContinenteRegion(Code='OCC',NomContinente='Europa', NombreReg='EUROPA OCCIDENTAL'),

                     ContinenteRegion(Code='AFR',NomContinente='Africa', NombreReg='AFRICA CENTRAL'),
                     ContinenteRegion(Code='AFEE',NomContinente='Africa', NombreReg='AFRICA DEL ESTE'),
                        ContinenteRegion(Code='AFN',NomContinente='Africa', NombreReg='AFRICA DEL NORTE'),
                        ContinenteRegion(Code='AFS',NomContinente='Africa', NombreReg='AFRICA DEL SUR'),
                        ContinenteRegion(Code='AFC',NomContinente='Africa', NombreReg='AFRICA OCCIDENTAL'),

                     ContinenteRegion(Code='CAR',NomContinente='Norte America', NombreReg='CARIBE'),
                        ContinenteRegion(Code='AMC',NomContinente='Norte America', NombreReg='AMERICA CENTRAL'),
                        ContinenteRegion(Code='AMN',NomContinente='Norte America', NombreReg='AMERICA DEL NORTE'),


                     ContinenteRegion(Code='SUA',NomContinente='Sur America', NombreReg='SUR AMERICA'),

                     ContinenteRegion(Code='ASO',NomContinente='Asia', NombreReg='ASIA ORIENTAL'),
                        ContinenteRegion(Code='ASE',NomContinente='Asia', NombreReg='ASIA DEL ESTE'),
                        ContinenteRegion(Code='ORM',NomContinente='Asia', NombreReg='ORIENTE MEDIO'),
                        ContinenteRegion(Code='SDA',NomContinente='Asia', NombreReg='SURESTE DE ASIA'),
                        ContinenteRegion(Code='SAC',NomContinente='Asia', NombreReg='SUR DE ASIA CENTRAL')]


#################################################### GET ########################################################################

@router.get("/ExamenParcial/C/continente/{NombreRegion}",status_code=200)
async def get_Continente(NombreRegion:str):
    if NombreRegion == 'region':
        return list_Continente_Region
    else:
        raise HTTPException(status_code=400, detail="URL Incorrecta, intentelo de nuevo")
    

#################################################### POST ########################################################################
@router.post("/ExamenParcial/C/continente/{NombreRegion}",status_code=201)
async def post_Continente(NombreRegion:str,NRegion:ContinenteRegion):
    found=False
    if NombreRegion == 'region':

        for index, save_region in enumerate(list_Continente_Region):
            if save_region.Code == NRegion.Code:
                raise HTTPException(status_code=400, detail="La Region ya existe")
        else:
            list_Continente_Region.append(NRegion)
            raise HTTPException(status_code=201, detail="Region creado exitosamente")
        
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    
#################################################### PUT ########################################################################
@router.put("/ExamenParcial/C/continente/{NombreRegion}",status_code=201)
async def put_Continente(NombreRegion:str,NRegion:ContinenteRegion):
    found=False

    if NombreRegion == 'region':
        for index, save_region in enumerate(list_Continente_Region):
            if save_region.Code == NRegion.Code:
                list_Continente_Region[index] = NRegion
                found=True
        if not found:
            raise HTTPException(status_code=404, detail="La Region No Existe")
        else:
            raise HTTPException(status_code=200, detail="La Region Fue Actualizado Exitosamente")
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    

#################################################### DELETE ########################################################################
@router.delete("/ExamenParcial/C/continente/{NombreRegion}/{Code}")
async def delete_Continente(NombreRegion:str,NRegion:ContinenteRegion, Code:str):
    found=False

    if NombreRegion == 'region':

        for index, saved_region in enumerate(list_Continente_Region):
            if saved_region.Code == Code:  #
                del list_Continente_Region[index]  
                found=True
                raise HTTPException(status_code=200, detail="La Region Fue Eliminado Exitosamente")
        
        if not found:
            raise HTTPException(status_code=204, detail="La Region No Existe")
        
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")