from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

#Se crea el router
router = APIRouter()

class Region(BaseModel): ##ENTIDAD
    Code:str
    Continente:str
    Nombre:str

list_Antartica = [Region(Code = 'ATA', Continente='Antarctica', Nombre= 'Antarctica'),
                  Region(Code = 'ATF', Continente='Antarctica', Nombre= 'French Southern Territories'),
                  Region(Code = 'BVT', Continente='Antarctica', Nombre= 'Bouvet Island'),
                  Region(Code = 'SGS', Continente='Antarctica', Nombre= 'South Georgia and the South Sandwich Islands'),
                  Region(Code = 'HMD',Continente='Antarctica', Nombre= 'Heard Island and McDonald Islands')]

list_Australia_NewZealand = [Region(Code = 'AUS', Continente='Oceania', Nombre= 'Australia'),
                            Region(Code = 'CXR', Continente='Oceania', Nombre= 'Christmas Island'),
                            Region(Code = 'CCK', Continente='Oceania', Nombre= 'Cocos (Keeling) Islands'),
                            Region(Code='NFK', Continente='Oceania', Nombre='Norfolk Island'),
                            Region(Code='NZL', Continente='Oceania', Nombre='New Zealand')]

list_Baltic = [Region(Code='EST', Continente='Europe', Nombre='Estonia'),
                Region(Code='LVA',Continente='Europe', Nombre='Latvia'),
                Region(Code='LTU', Continente='Europe', Nombre='Lithuania')]

list_British = [Region(Code='GBR', Continente='Europe', Nombre='United Kingdom'),
                Region(Code='IRL', Continente='Europe', Nombre='Ireland')]

list_Caribbean =[Region(Code='ABW',Continente='North America', Nombre='Aruba'),
                 Region(Code='AIA', Continente='North America', Nombre='Anguilla'),
                 Region(Code='ANT', Continente='North America', Nombre='Netherlands Antilles'),
                 Region(Code='ATG', Continente='North America', Nombre='Antigua and Barbuda'),
                 Region(Code='BHS', Continente='North America', Nombre='Bahamas'),
                 Region(Code='BRB', Continente='North America', Nombre='Barbados'),
                 Region(Code='CUB', Continente='North America', Nombre='Cuba'),
                 Region(Code='CYM', Continente='North America', Nombre='Cayman Islands'),
                 Region(Code='DMA', Continente='North America', Nombre='Dominica'),
                 Region(Code='DOM', Continente='North America', Nombre='Dominican Republic'),
                 Region(Code='GRD', Continente='North America', Nombre='Grenada'),
                 Region(Code='GLP', Continente='North America', Nombre='Guadeloupe'),
                 Region(Code='HTI', Continente='North America', Nombre='Haiti'),
                 Region(Code='JAM', Continente='North America', Nombre='Jamaica'),
                 Region(Code='MTQ', Continente='North America', Nombre='Martinique'),
                 Region(Code='MSR', Continente='North America', Nombre='Montserrat'),
                 Region(Code='PRI', Continente='North America', Nombre='Puerto Rico'),
                 Region(Code='KNA', Continente='North America', Nombre='Saint Kitts and Nevis'),
                 Region(Code='LCA', Continente='North America', Nombre='Saint Lucia'),
                 Region(Code='VCT', Continente='North America', Nombre='Saint Vincent and the Grenadines'),
                 Region(Code='TTO', Continente='North America', Nombre='Trinidad and Tobago'),
                 Region(Code='TCA', Continente='North America', Nombre='Turks and Caicos Islands'),
                 Region(Code='VIR', Continente='North America', Nombre='U.S. Virgin Islands'),
                 Region(Code='VGB', Continente='North America', Nombre='British Virgin Islands')]

list_CentralAfrica =[Region(Code='AGO',Continente='Africa', Nombre='Angola'),
                     Region(Code='CMR', Continente='Africa', Nombre='Cameroon'),
                     Region(Code='CAF', Continente='Africa', Nombre='Central African Republic'),
                     Region(Code='COG', Continente='Africa', Nombre='Congo'),
                     Region(Code='COD', Continente='Africa', Nombre='Congo, The Democratic Republic of the'),
                     Region(Code='GNQ', Continente='Africa', Nombre='Equatorial Guinea'),
                     Region(Code='GAB', Continente='Africa', Nombre='Gabon'),
                     Region(Code='STP', Continente='Africa', Nombre='Sao Tome and Principe'),
                     Region(Code='TCD', Continente='Africa', Nombre='Chad')]

list_CentralAmerica =[Region(Code='BLZ',Continente='North America', Nombre='Belize'),
                        Region(Code='CRI', Continente='North America', Nombre='Costa Rica'),
                        Region(Code='SLV', Continente='North America', Nombre='El Salvador'),
                        Region(Code='GTM', Continente='North America', Nombre='Guatemala'),
                        Region(Code='HND', Continente='North America', Nombre='Honduras'),
                        Region(Code='MEX', Continente='North America', Nombre='Mexico'),
                        Region(Code='NIC', Continente='North America', Nombre='Nicaragua'),
                        Region(Code='PAN', Continente='North America', Nombre='Panama')]


list_EastAsia =[Region(Code='CHN',Continente='Asia', Nombre='China'),
                Region(Code='HKG', Continente='Asia', Nombre='Hong Kong'),
                Region(Code='JPN', Continente='Asia', Nombre='Japan'),
                Region(Code='KOR', Continente='Asia', Nombre='South Korea'),
                Region(Code='MAC', Continente='Asia', Nombre='Macao'),
                Region(Code='MNG', Continente='Asia', Nombre='Mongolia'),
                Region(Code='PRK', Continente='Asia', Nombre='Korea, Democratic Peoples Republic of'),
                Region(Code='TWN', Continente='Asia', Nombre='Taiwan')]

list_EastEurope =[Region(Code='BLR',Continente='Europe', Nombre='Belarus'),
                    Region(Code='BGR', Continente='Europe', Nombre='Bulgaria'),
                    Region(Code='EST', Continente='Europe', Nombre='Estonia'),
                    Region(Code='CZE', Continente='Europe', Nombre='Czech Republic'),
                    Region(Code='GEO', Continente='Europe', Nombre='Georgia'),
                    Region(Code='HUN', Continente='Europe', Nombre='Hungary'),
                    Region(Code='MDA', Continente='Europe', Nombre='Moldova'),
                    Region(Code='POL', Continente='Europe', Nombre='Poland'),
                    Region(Code='ROU', Continente='Europe', Nombre='Romania'),
                    Region(Code='RUS', Continente='Europe', Nombre='Russian Federation'),
                    Region(Code='SVK', Continente='Europe', Nombre='Slovakia'),
                    Region(Code='UKR', Continente='Europe', Nombre='Ukraine')]

list_EastAfrica =[Region(Code='BDI',Continente='Africa', Nombre='Burundi'),
                    Region(Code='COM', Continente='Africa', Nombre='Comoros'),
                    Region(Code='DJI', Continente='Africa', Nombre='Djibouti'),
                    Region(Code='ERI', Continente='Africa', Nombre='Eritrea'),  
                    Region(Code='ETH', Continente='Africa', Nombre='Ethiopia'),
                    Region(Code='IOT', Continente='Africa', Nombre='British Indian Ocean Territory'),
                    Region(Code='KEN', Continente='Africa', Nombre='Kenya'),
                    Region(Code='MDG', Continente='Africa', Nombre='Madagascar'),
                    Region(Code='MWI', Continente='Africa', Nombre='Malawi'),
                    Region(Code='MUS', Continente='Africa', Nombre='Mauritius'),
                    Region(Code='MYT', Continente='Africa', Nombre='Mayotte'),
                    Region(Code='MOZ', Continente='Africa', Nombre='Mozambique'),
                    Region(Code='REU', Continente='Africa', Nombre='Reunion'),
                    Region(Code='RWA', Continente='Africa', Nombre='Rwanda'),
                    Region(Code='SYC', Continente='Africa', Nombre='Seychelles'),
                    Region(Code='SOM', Continente='Africa', Nombre='Somalia'),
                    Region(Code='TZA', Continente='Africa', Nombre='Tanzania, United Republic of'),
                    Region(Code='UGA', Continente='Africa', Nombre='Uganda'),
                    Region(Code='ZMB', Continente='Africa', Nombre='Zambia'),
                    Region(Code='ZWE', Continente='Africa', Nombre='Zimbabwe')]

list_Melanesia = [Region(Code='FJI',Continente='Oceania', Nombre='Fiji Islands'),
                    Region(Code='NCL', Continente='Oceania', Nombre='New Caledonia'),
                    Region(Code='PNG', Continente='Oceania', Nombre='Papua New Guinea'),
                    Region(Code='SLB', Continente='Oceania', Nombre='Solomon Islands'),
                    Region(Code='VUT', Continente='Oceania', Nombre='Vanuatu')]

list_Micronesia = [Region(Code='FSM',Continente='Oceania', Nombre='Micronesia, Federated States of'),
                    Region(Code='GUM', Continente='Oceania', Nombre='Guam'),
                    Region(Code='KIR', Continente='Oceania', Nombre='Kiribati'),
                    Region(Code='MHL', Continente='Oceania', Nombre='Marshall Islands'),
                    Region(Code='MNP', Continente='Oceania', Nombre='Northern Mariana Islands'),
                    Region(Code='NRU', Continente='Oceania', Nombre='Nauru'),
                    Region(Code='PLW', Continente='Oceania', Nombre='Palau')]

list_MiddleEast = [Region(Code='ARE', Continente='Asia', Nombre='united Arab Emirates'),
                    Region(Code='ARM', Continente='Asia', Nombre='Armenia'),
                    Region(Code='AZE', Continente='Asia', Nombre='Azerbaijan'),
                    Region(Code='BHR', Continente='Asia', Nombre='Bahrain'),
                    Region(Code='CYP', Continente='Asia', Nombre='Cyprus'),
                    Region(Code='GEO', Continente='Asia', Nombre='Georgia'),
                    Region(Code='IRQ', Continente='Asia', Nombre='Iraq'),
                    Region(Code='JOR', Continente='Asia', Nombre='Jordan'),
                    Region(Code='KWT', Continente='Asia', Nombre='Kuwait'),
                    Region(Code='LBN', Continente='Asia', Nombre='Lebanon'),
                    Region(Code='OMN', Continente='Asia', Nombre='Oman'),
                    Region(Code='PSE', Continente='Asia', Nombre='Palestine'),
                    Region(Code='QAT', Continente='Asia', Nombre='Qatar'),
                    Region(Code='SAU', Continente='Asia', Nombre='Saudi Arabia'),
                    Region(Code='SYR', Continente='Asia', Nombre='Syria'),
                    Region(Code='TUR', Continente='Asia', Nombre='Turkey'),
                    Region(Code='YEM', Continente='Asia', Nombre='Yemen')]

list_Nordic = [Region(Code='DNK', Continente='Europe', Nombre='Denmark'),
                Region(Code='FIN', Continente='Europe', Nombre='Finland'),
                Region(Code='FRO', Continente='Europe', Nombre='Farao Islands'),
                Region(Code='ISL', Continente='Europe', Nombre='Iceland'),
                Region(Code='NOR', Continente='Europe', Nombre='Norway'),
                Region(Code='SJM', Continente='Europe', Nombre='Svalbard and Jan Mayen'),
                Region(Code='SWE', Continente='Europe', Nombre='Sweden')]

list_NorthAmerica = [Region(Code='BMU', Continente='North America', Nombre='Bermuda'),
                    Region(Code='CAN', Continente='North America', Nombre='Canada'),
                    Region(Code='GRL', Continente='North America', Nombre='Greenland'),
                    Region(Code='SPM', Continente='North America', Nombre='Saint Pierre and Miquelon'),
                    Region(Code='USA', Continente='North America', Nombre='United States')]

list_NorthAfrica= [Region(Code='DZA', Continente='Africa', Nombre='Algeria'),
                    Region(Code='EGY', Continente='Africa', Nombre='Egypt'),
                    Region(Code='ESH', Continente='Africa', Nombre='Western Sahara'),
                    Region(Code='LBY', Continente='Africa', Nombre='Libyan Arab Jamahiriya'),
                    Region(Code='MAR', Continente='Africa', Nombre='Morocco'),
                    Region(Code='SDN', Continente='Africa', Nombre='Sudan'),
                    Region(Code='TUN', Continente='Africa', Nombre='Tunisia')]
                   

list_Polynesia = [Region(Code='ASM', Continente='Oceania', Nombre='American Samoa'),
                         Region(Code='COK', Continente='Oceania', Nombre='Cook Islands'),
                         Region(Code='NIU', Continente='Oceania', Nombre='Niue'),
                         Region(Code='PCN', Continente='Oceania', Nombre='Pitcairn'),
                        Region(Code='PYF', Continente='Oceania', Nombre='French Polynesia'),                         
                         Region(Code='TKL', Continente='Oceania', Nombre='Tokelau'),
                         Region(Code='TON', Continente='Oceania', Nombre='Tonga'),
                         Region(Code='TUV', Continente='Oceania', Nombre='Tuvalu'),
                        Region(Code='WLF', Continente='Oceania', Nombre='Wallis and Futuna'),
                        Region(Code='WSM', Continente='Oceania', Nombre='Samoa')]

list_SouthAmerica = [Region(Code='ARG', Continente='South America', Nombre='Argentina'),
                    Region(Code='BOL', Continente='South America', Nombre='Bolivia'),
                    Region(Code='BRA', Continente='South America', Nombre='Brazil'),
                    Region(Code='CHL', Continente='South America', Nombre='Chile'),
                    Region(Code='COL', Continente='South America', Nombre='Colombia'),
                    Region(Code='ECU', Continente='South America', Nombre='Ecuador'),
                    Region(Code='FLK', Continente='South America', Nombre='Falkland Islands (Malvinas)'),
                    Region(Code='GUF', Continente='South America', Nombre='French Guiana'),
                    Region(Code='GUY', Continente='South America', Nombre='Guyana'),
                    Region(Code='PRY', Continente='South America', Nombre='Paraguay'),
                    Region(Code='PER', Continente='South America', Nombre='Peru'),
                    Region(Code='SUR', Continente='South America', Nombre='Suriname'),
                    Region(Code='URY', Continente='South America', Nombre='Uruguay'),
                    Region(Code='VEN', Continente='South America', Nombre='Venezuela')]

list_SoutheastAsia = [Region(Code='BRN', Continente='Asia', Nombre='Brunei'),
                    Region(Code='IDN', Continente='Asia', Nombre='Indonesia'),
                    Region(Code='KHM', Continente='Asia', Nombre='Cambodia'),
                    Region(Code='LAO', Continente='Asia', Nombre='Laos'),
                    Region(Code='MYS', Continente='Asia', Nombre='Malaysia'),
                    Region(Code='MMR', Continente='Asia', Nombre='Myanmar'),
                    Region(Code='PHL', Continente='Asia', Nombre='Philippines'),

                    Region(Code='SGP', Continente='Asia', Nombre='Singapore'),
                    Region(Code='THA', Continente='Asia', Nombre='Thailand'),
                    Region(Code='TLS', Continente='Asia', Nombre='Timor-Leste'),
                    Region(Code='VNM', Continente='Asia', Nombre='Vietnam')]

list_SouthernAfrica = [Region(Code='BWA', Continente='Africa', Nombre='Botswana'),
                       Region(Code='LSO', Continente='Africa', Nombre='Lesotho'),
                       Region(Code='NAM', Continente='Africa', Nombre='Namibia'),
                       Region(Code='ZAF', Continente='Africa', Nombre='South Africa'),
                       Region(Code='SWZ', Continente='Africa', Nombre='Swaziland')]

list_SouthernCentralAsia = [Region(Code='AFG', Continente='Asia', Nombre='Afghanistan'),
                            Region(Code='BGD', Continente='Asia', Nombre='Bangladesh'),
                            Region(Code='BTN', Continente='Asia', Nombre='Bhutan'),
                            Region(Code='IND', Continente='Asia', Nombre='India'),
                            Region(Code='IRN', Continente='Asia', Nombre='Iran'),
                            Region(Code='KAZ', Continente='Asia', Nombre='Kazakstan'),
                            Region(Code='KGZ', Continente='Asia', Nombre='Kyrgyzstan'),
                            Region(Code = 'LKA', Continente='Asia', Nombre = 'Sri Lanka'),
                            Region(Code='MDV', Continente='Asia', Nombre='Maldives'),
                            Region(Code='NPL', Continente='Asia', Nombre='Nepal'),
                            Region(Code='PAK', Continente='Asia', Nombre='Pakistan'),
                            Region(Code='TJK', Continente='Asia', Nombre='Tajikistan'),
                            Region(Code='TKM', Continente='Asia', Nombre='Turkmenistan'),
                            Region(Code='UZB', Continente='Asia', Nombre='Uzbekistan')]

list_SouthernEurope = [Region(Code='ALB', Continente='Europe', Nombre='Albania'),
                        Region(Code='AND', Continente='Europe', Nombre='Andorra'),
                        Region(Code='BIH', Continente='Europe', Nombre='Bosnia and Herzegovina'),
                        Region(Code='ESP', Continente='Europe', Nombre='Spain'),
                        Region(Code='GIB', Continente='Europe', Nombre='Gibraltar'),
                        Region(Code='GRC', Continente='Europe', Nombre='Greece'),
                        Region(Code='HRV', Continente='Europe', Nombre='Croatia'),
                        Region(Code='ITA', Continente='Europe', Nombre='Italy'),
                        Region(Code='MKD', Continente='Europe', Nombre='Macedonia'),
                        Region(Code='MLT', Continente='Europe', Nombre='Malta'),
                        Region(Code='PRT', Continente='Europe', Nombre='Portugal'),
                        Region(Code='SMR', Continente='Europe', Nombre='San Marino'),
                        Region(Code='SVN', Continente='Europe', Nombre='Slovenia'),
                        Region(Code='VAT', Continente='Europe', Nombre='Holy See (Vatican City State)'),
                        Region(Code='YUG', Continente='Europe', Nombre='Yugoslavia')]

list_WesternAfrica = [Region(Code='BEN', Continente='Africa', Nombre='Benin'),
                      Region(Code='BFA', Continente='Africa', Nombre='Burkina Faso'),
                      Region(Code='CIV', Continente='Africa', Nombre='Cote d\'Ivoire'),
                      Region(Code='CPV', Continente='Africa', Nombre='Cape Verde'),
                      Region(Code='GMB', Continente='Africa', Nombre='Gambia'),
                      Region(Code='GHA', Continente='Africa', Nombre='Ghana'),
                      Region(Code='GIN', Continente='Africa', Nombre='Guinea'),
                      Region(Code='GNB', Continente='Africa', Nombre='Guinea-Bissau'),
                      Region(Code='LBR', Continente='Africa', Nombre='Liberia'),
                      Region(Code='MLI', Continente='Africa', Nombre='Mali'),
                      Region(Code='MRT', Continente='Africa', Nombre='Mauritania'),
                      Region(Code='NER', Continente='Africa', Nombre='Niger'),
                      Region(Code='NGA', Continente='Africa', Nombre='Nigeria'),
                      Region(Code='SHN', Continente='Africa', Nombre='Saint Helena'),
                      Region(Code='SEN', Continente='Africa', Nombre='Senegal'),
                      Region(Code='SLE', Continente='Africa', Nombre='Sierra Leone'),
                      Region(Code='TGO', Continente='Africa', Nombre='Togo')]

list_WesternEurope = [Region(Code='AUT', Continente='Europe', Nombre='Austria'),
                      Region(Code='BEL', Continente='Europe', Nombre='Belgium'),
                      Region(Code='CHE', Continente='Europe', Nombre='Switzerland'),
                      Region(Code='DEU', Continente='Europe', Nombre='Germany'),
                      Region(Code='FRA', Continente='Europe', Nombre='France'),
                      Region(Code='LIE', Continente='Europe', Nombre='Liechtenstein'),
                    Region(Code='LUX', Continente='Europe', Nombre='Luxembourg'),
                    Region(Code='MCO', Continente='Europe', Nombre='Monaco'),
                    Region(Code='NLD', Continente='Europe', Nombre='Netherlands')
                      ]

####################################### GET ###########################################
##configurar A,B,C,D PARA PODER ESCRIBIR UN URL NO EXISTENTE
@router.get("/ExamenParcial/D/{Region}", status_code=200)
async def get_region(Region: str):
    if Region == 'antartida':
      return list_Antartica
    elif Region == 'australia':
       return list_Australia_NewZealand
    elif Region == 'baltico':
       return list_Baltic
    elif Region == 'britanico':
       return list_British
    elif Region == 'caribe':
       return list_Caribbean
    elif Region == 'africacentral':
        return list_CentralAfrica
    elif Region == 'americacentral':
       return list_CentralAmerica
    elif Region == 'asiadeleste':
       return list_EastAsia
    elif Region == 'europadeleste':
       return list_EastEurope
    elif Region == 'africadeleste':
       return list_EastAfrica
    elif Region == 'melanesia':
       return list_Melanesia
    elif Region == 'micronesia':
       return list_Micronesia
    elif Region == 'medioeste':
       return list_MiddleEast
    elif Region == 'nordico':
       return list_Nordic
    elif Region == 'norteamerica':
       return list_NorthAmerica
    elif Region == 'africadelnorte':
       return list_NorthAfrica
    elif Region == 'polinesia':
       return list_Polynesia
    elif Region == 'sudamerica':
       return list_SouthAmerica
    elif Region == 'surestedeasia':
       return list_SoutheastAsia
    elif Region == 'suroestedeafrica':
       return list_SouthernAfrica
    elif Region == 'suroestecentraldeasia':
       return list_SouthernCentralAsia
    elif Region == 'surestedeeuropa':
       return list_SouthernEurope
    elif Region == 'africaoccidental':
        return list_WesternAfrica
    elif Region == 'europaoccidental':
        return list_WesternEurope
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El continente no existe")
    
####################################### POST ###########################################
@router.post("/ExamenParcial/D/{NomRegion}", status_code=201)
async def post_region(NomRegion: str, region: Region):
   if NomRegion == 'antartida':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="El pais ya existe")
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Antartica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'australia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta region ya existe")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Australia_NewZealand.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
   
   elif NomRegion == 'baltico':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region ya existe" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Baltic.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'britanico':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region ya existe" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_British.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'caribe':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region ya existe" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Caribbean.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'africacentral':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_CentralAfrica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'americacentral':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_CentralAmerica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'asiadeleste':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_EastAsia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'europadeleste':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_EastEurope.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'europadeleeste':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_EastEurope.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'africadeleste':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_EastAfrica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
   
   elif NomRegion == 'melanesia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Melanesia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'micronesia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Micronesia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'medioeste':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_MiddleEast.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'nordico':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Nordic.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
   
   elif NomRegion == 'norteamerica':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertence Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_NorthAmerica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'africadelnorte':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_NorthAfrica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'polinesia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_Polynesia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'sudamerica':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_SouthAmerica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )

   elif NomRegion == 'surestedeasia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_SoutheastAsia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'suroestedeafrica':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_SouthernAfrica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'suroestecentraldeasia':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_SouthernCentralAsia.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'surestedeeuropa':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_SouthernEurope.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'africaoccidental':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      else:
            list_WesternAfrica.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
      
   elif NomRegion == 'europaoccidental':
      for index, save_region in enumerate(list_Antartica):
         if save_region.Code == region.Code:
            raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Australia_NewZealand):
         if save_region.Code == region.Code:
            raise HTTPException(status_code=400, detail="Esta Region No pertenece Aqui!!")
      for index, save_region in enumerate(list_Baltic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_British):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Caribbean):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_CentralAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No Pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_EastAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Melanesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Micronesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_MiddleEast):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Nordic):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_NorthAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_Polynesia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthAmerica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SoutheastAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernCentralAsia):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_SouthernEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternAfrica):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "Esta Region No pertenece Aqui!!" )
      for index, save_region in enumerate(list_WesternEurope):
            if save_region.Code == region.Code:
                raise HTTPException(status_code = 400, detail= "La Region Ya Existe" )
      else:
            list_WesternEurope.append(region)
            raise HTTPException(status_code = 201, detail= "Region Creada Con Exito!!" )
   else:
      raise HTTPException(status_code = 404, detail= "URL Incorrecta, intentelo de nuevo" )

################################################ PUT ###############################################
##Crear El Metodo de PUT
@router.put('/ExamenParcial/D/{NomRegion}')
async def update_region(NomRegion: str, region: Region):
      found = False

      if NomRegion == 'antartida':
            for index, save_region in enumerate(list_Antartica):
                  if save_region.Code == region.Code:
                        list_Antartica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      
      elif NomRegion == 'australia':
            for index, save_region in enumerate(list_Australia_NewZealand):
                  if save_region.Code == region.Code:
                        list_Australia_NewZealand[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
            
      elif NomRegion == 'baltico':
            for index, save_region in enumerate(list_Baltic):
                  if save_region.Code == region.Code:
                        list_Baltic[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == ' britanico':
            for index, save_region in enumerate(list_British):
                  if save_region.Code == region.Code:
                        list_British[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'caribe':
            for index, save_region in enumerate(list_Caribbean):
                  if save_region.Code == region.Code:
                        list_Caribbean[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'africacentral':
            for index, save_region in enumerate(list_CentralAfrica):
                  if save_region.Code == region.Code:
                        list_CentralAfrica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'americacentral':
            for index, save_region in enumerate(list_CentralAmerica):
                  if save_region.Code == region.Code:
                        list_CentralAmerica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'asiadeleeste':
            for index, save_region in enumerate(list_EastAsia):
                  if save_region.Code == region.Code:
                        list_EastAsia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'europadeleste': 
            for index, save_region in enumerate(list_EastEurope):
                  if save_region.Code == region.Code:
                        list_EastEurope[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'africadeleste':
            for index, save_region in enumerate(list_EastAfrica):
                  if save_region.Code == region.Code:
                        list_EastAfrica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'melanesia':
            for index, save_region in enumerate(list_Melanesia):
                  if save_region.Code == region.Code:
                        list_Melanesia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'micronesia':
            for index, save_region in enumerate(list_Micronesia):
                  if save_region.Code == region.Code:
                        list_Micronesia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'nordico':
            for index, save_region in enumerate(list_Nordic):
                  if save_region.Code == region.Code:
                        list_Nordic[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'norteamerica':
            for index, save_region in enumerate(list_NorthAmerica):
                  if save_region.Code == region.Code:
                        list_NorthAmerica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'africadelnorte':
            for index, save_region in enumerate(list_NorthAfrica):
                  if save_region.Code == region.Code:
                        list_NorthAfrica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'polinesia':
            for index, save_region in enumerate(list_Polynesia):
                  if save_region.Code == region.Code:
                        list_Polynesia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'sudamerica':
            for index, save_region in enumerate(list_SouthAmerica):
                  if save_region.Code == region.Code:
                        list_SouthAmerica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'surestedeasia':
            for index, save_region in enumerate(list_SoutheastAsia):
                  if save_region.Code == region.Code:
                        list_SoutheastAsia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'suroestedeafrica':
            for index, save_region in enumerate(list_SouthernAfrica):
                  if save_region.Code == region.Code:
                        list_SouthernAfrica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'suroestecentraldeasia':
            for index, save_region in enumerate(list_SouthernCentralAsia):
                  if save_region.Code == region.Code:
                        list_SouthernCentralAsia[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'surestedeeuropa':
            for index, save_region in enumerate(list_SouthernEurope):
                  if save_region.Code == region.Code:
                        list_SouthernEurope[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'africaoccidental':
            for index, save_region in enumerate(list_WesternAfrica):
                  if save_region.Code == region.Code:
                        list_WesternAfrica[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      elif NomRegion == 'europaoccidental':
            for index, save_region in enumerate(list_WesternEurope):
                  if save_region.Code == region.Code:
                        list_WesternEurope[index] = region
                        found =True
            if not found:
                  raise HTTPException(status_code = 404, detail= "La Region No Existe" )
            else:
                  raise HTTPException(status_code = 201, detail= "La Region Fue Actualizada Con Exito!!" )
      else:
            raise HTTPException(status_code = 404, detail= "URL Incorrecta, intentelo de nuevo" )
      
####################################################### DELETE ###########################################################
@router.delete("/ExamenParcial/D/{NomRegion}/{Code}")
async def delete_region(NomRegion: str, Code: str):
      found=False
      if NomRegion == 'antartida':
            for index,  save_region in enumerate(list_Antartica):
                  if  save_region.Code == Code:
                        del list_Antartica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'australia':
            for index,  save_region in enumerate(list_Australia_NewZealand):
                  if  save_region.Code == Code:
                        del list_Australia_NewZealand[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'baltico':
            for index,  save_region in enumerate(list_Baltic):
                  if  save_region.Code == Code:
                        del list_Baltic[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'britanico':
            for index,  save_region in enumerate(list_British):
                  if  save_region.Code == Code:
                        del list_British[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'caribe':
            for index,  save_region in enumerate(list_Caribbean):
                  if  save_region.Code == Code:
                        del list_Caribbean[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'africacentral':
            for index,  save_region in enumerate(list_CentralAfrica):
                  if  save_region.Code == Code:
                        del list_CentralAfrica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'americacentral':
            for index,  save_region in enumerate(list_CentralAmerica):
                  if  save_region.Code == Code:
                        del list_CentralAmerica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'asiadeleste':
            for index,  save_region in enumerate(list_EastAsia):
                  if  save_region.Code == Code:
                        del list_EastAsia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'europadeleste':
            for index,  save_region in enumerate(list_EastEurope):
                  if  save_region.Code == Code:
                        del list_EastEurope[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'africadeleste':
            for index,  save_region in enumerate(list_EastAfrica):
                  if  save_region.Code == Code:
                        del list_EastAfrica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'melanesia':
            for index,  save_region in enumerate(list_Melanesia):
                  if  save_region.Code == Code:
                        del list_Melanesia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'micronesia':
            for index,  save_region in enumerate(list_Micronesia):
                  if  save_region.Code == Code:
                        del list_Micronesia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'medioeste':
            for index,  save_region in enumerate(list_MiddleEast):
                  if  save_region.Code == Code:
                        del list_MiddleEast[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'nordico':
            for index,  save_region in enumerate(list_Nordic):
                  if  save_region.Code == Code:
                        del list_Nordic[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'norteamerica':
            for index,  save_region in enumerate(list_NorthAmerica):
                  if  save_region.Code == Code:
                        del list_NorthAmerica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'africadelnorte':
            for index,  save_region in enumerate(list_NorthAfrica):
                  if  save_region.Code == Code:
                        del list_NorthAfrica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'polinesia':
            for index,  save_region in enumerate(list_Polynesia):
                  if  save_region.Code == Code:
                        del list_Polynesia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'sudamerica':
            for index,  save_region in enumerate(list_SouthAmerica):
                  if  save_region.Code == Code:
                        del list_SouthAmerica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'surestedeasia':
            for index,  save_region in enumerate(list_SoutheastAsia):
                  if  save_region.Code == Code:
                        del list_SoutheastAsia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'suroestedeafrica':
            for index,  save_region in enumerate(list_SouthernAfrica):
                  if  save_region.Code == Code:
                        del list_SouthernAfrica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'suroestecentraldeasia':
            for index,  save_region in enumerate(list_SouthernCentralAsia):
                  if  save_region.Code == Code:
                        del list_SouthernCentralAsia[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'surestedeeuropa':
            for index,  save_region in enumerate(list_SouthernEurope):
                  if  save_region.Code == Code:
                        del list_SouthernEurope[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'africaoccidental':
            for index,  save_region in enumerate(list_WesternAfrica):
                  if  save_region.Code == Code:
                        del list_WesternAfrica[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
      elif NomRegion == 'europaoccidental':
            for index,  save_region in enumerate(list_WesternEurope):
                  if  save_region.Code == Code:
                        del list_WesternEurope[index]
                        found=True
            if not found:
                  raise HTTPException(status_code = 204, detail= "Esta Region No Existe!!" )
            else:
                  raise HTTPException(status_code = 200, detail= "Esta Region Fue Eliminada!!" )
            
            
            
            
            
           
          

            
      
