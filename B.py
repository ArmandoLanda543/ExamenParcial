from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class Region(BaseModel): ##ENTIDAD
    Code:str
    Nombre:str

list_Africa =[Region(Code = 'CA', Nombre = 'Central Africa'),
            Region(Code = 'EA', Nombre = 'Eastern Africa'),
            Region( Code = 'NA', Nombre = 'Northern Africa'),
            Region( Code = 'SA', Nombre = 'Southern Africa'),
            Region( Code = 'WA', Nombre = 'Western Africa')]

list_Europe =[Region(Code = 'EE', Nombre = 'Eastern Europe'),
            Region(Code = 'NE', Nombre = 'Northern Europe'),
            Region(Code = 'SE', Nombre = 'Southern Europe'),
            Region(Code = 'WE', Nombre = 'Western Europe'),
            Region(Code = 'NO', Nombre = 'Nordic Countries'),
            Region(Code = 'BC', Nombre = 'Baltic Countries'),
            Region(Code = 'BI', Nombre = 'British Islands')]

list_NorthAmerica =[Region(Code = 'CAR', Nombre = 'Caribbean'),
            Region(Code = 'ENA', Nombre = 'Central America'),
            Region(Code = 'NNA', Nombre = 'North America')]

list_SouthAmerica =[Region(Code = 'CSA', Nombre = 'South America')]

list_Oceania =[Region(Code = 'POL', Nombre = 'Polynesia'),
            Region(Code = 'AUSNZ', Nombre = 'Australia and New Zealand'),
            Region(Code = 'MEL', Nombre = 'Melanesia'),
            Region(Code = 'MIC', Nombre = 'Micronesia'),
            Region(Code = 'MICCAR', Nombre = 'Micronesia\/Caribbean')]

list_Antarctica =[Region(Code = 'CA', Nombre = 'Antarctica')]

list_Asia =[Region(Code = 'SCA', Nombre = 'Southern and Central Asia'),
            Region(Code = 'ME', Nombre = 'Middle East'),
            Region(Code = 'SOA', Nombre = 'Southeast Asia'),
            Region(Code = 'EA', Nombre = 'Eastern Asia')]

#################################################### GET ########################################################################

@router.get("/ExamenParcial/B/{NomContinente}",status_code=200)
async def get_Region(NomContinente:str):

    if NomContinente == 'africa':
        return list_Africa
    elif NomContinente == 'europa':
        return list_Europe
    elif NomContinente == 'norteamerica':
        return list_NorthAmerica
    elif NomContinente == 'sudamerica':
        return list_SouthAmerica
    elif NomContinente == 'oceania':
        return list_Oceania
    elif NomContinente == 'antartida':
        return list_Antarctica
    elif NomContinente == 'asia':
        return list_Asia
    else:
        raise HTTPException(status_code=404, detail="URL Incorrecta, intentelo de nuevo")
    

##################################################### POST ########################################################################
@router.post("/ExamenParcial/B/{NomContinente}",status_code=201)
async def post_Region(NomContinente:str,region:Region):

    if NomContinente == 'africa':
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_Africa.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
        
    elif NomContinente == 'europa':
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_Europe.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
        
    elif NomContinente == 'norteamerica':
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_NorthAmerica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
        
    elif NomContinente == 'sudamerica':
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_SouthAmerica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
        
    elif NomContinente == 'oceania':
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_Oceania.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
        
    elif NomContinente == 'antartida':
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_Antarctica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
        
    elif NomContinente == 'asia':
        for index, save_region in enumerate(list_Asia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region Ya Existe!!" )
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Europe):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Oceania):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        for index, save_region in enumerate(list_Antarctica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
        else:
            list_Asia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
            return region
    else:
        raise HTTPException(status_code = 404, detail= "URL Incorrecta, intentelo de nuevo" )
    
##################################################### PUT #####################################################
@router.put("/ExamenParcial/B/{NomContinente}")
async def put_region(NomContinente:str,region:Region):
    found = False

    if NomContinente == 'africa':
        for index, save_region in enumerate(list_Africa):
            if save_region.Code == region.Code:
                list_Africa[index] = region
                found=True
        if not found:
            raise HTTPException(status_code=404, detail="Esta Region No Existe!!")
        else:
            raise HTTPException(status_code=200, detail="El continente Fue Actualizado Exitosamente")


    elif NomContinente == 'europa':
        for index,  save_region in enumerate(list_Europe):
              if  save_region.Code == region.Code:
                list_Europe[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
        
    elif NomContinente == 'norteamerica':
        for index,  save_region in enumerate(list_NorthAmerica):
              if  save_region.Code == region.Code:
                list_NorthAmerica[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
        
    elif NomContinente == 'sudamerica':
        for index,  save_region in enumerate(list_SouthAmerica):
              if  save_region.Code == region.Code:
                list_SouthAmerica[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
        
    elif NomContinente == 'oceania':
        for index,  save_region in enumerate(list_Oceania):
              if  save_region.Code == region.Code:
                list_Oceania[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
        
    elif NomContinente == 'antartida':
        for index,  save_region in enumerate(list_Antarctica):
              if  save_region.Code == region.Code:
                list_Antarctica[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
        
    elif NomContinente == 'asia':
        for index,  save_region in enumerate(list_Asia):
              if  save_region.Code == region.Code:
                list_Asia[index] = region
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Ya Fue Actualizada!!" )
  
    else:
        raise HTTPException(status_code = 404, detail= "URL Incorrecta, intentelo de nuevo" )
##################################################### DELETE #####################################################
@router.delete("/ExamenParcial/B/{NomContinente}/{Code}")
async def delete_region(NomContinente: str, Code: str):
    found = False
    if NomContinente == 'africa':
        for index,  save_region in enumerate(list_Africa):
            if  save_region.Code == Code:
                del list_Africa[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )

    elif NomContinente == 'europa':
        for index,  save_region in enumerate(list_Europe):
              if  save_region.Code == Code:
                del list_Europe[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
        
    elif NomContinente == 'norteamerica':
        for index,  save_region in enumerate(list_NorthAmerica):
              if  save_region.Code == Code:
                del list_NorthAmerica[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
        
    elif NomContinente == 'sudamerica':
        for index,  save_region in enumerate(list_SouthAmerica):
              if  save_region.Code == Code:
                del list_SouthAmerica[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
        
    elif NomContinente == 'oceania':
        for index,  save_region in enumerate(list_Oceania):
              if  save_region.Code == Code:
                del list_Oceania [index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
        
    elif NomContinente == 'antartida':
        for index,  save_region in enumerate(list_Antarctica):
              if  save_region.Code == Code:
                del list_Antarctica[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
        
    elif NomContinente == 'asia':
        for index,  save_region in enumerate(list_Asia):
              if  save_region.Code == Code:
                del list_Asia[index]
                found=True
        if not found:
            raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
        else:
            raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )

