from fastapi import FastAPI, HTTPException, status
import A,B,C,D, E
from pydantic import BaseModel
#Importamos la librerias

app=FastAPI()

#Incluir las demás libreria
app.include_router(A.router)
app.include_router(B.router)
app.include_router(C.router)
app.include_router(D.router)
app.include_router(E.router)


############################################################ CLASS #########################################################################

class Pais(BaseModel): ##ENTIDAD
    Code:str
    Nombre:str
    Continente:str
    Region:str
    Superficie:int
    AñoInde:int
    Poblacion:int
    EsperanzaVida:float
    NombreLocal:str
    Gobierno:str    
    Presidente:str

list_Pais1 = [Pais( Code='ABW', Nombre='Aruba', Continente='North America', Region='Caribbean', Superficie='193', AñoInde='0', Poblacion='103000', EsperanzaVida='78.4', NombreLocal= 'Aruba', Gobierno='Nonmetropolitan Territory of The Netherlands', Presidente='Willem-Alexander')]
list_Pais2 =  [Pais(    Code='AFG',Nombre='Afghanistan', Continente='Asia', Region='Southern and Central Asia', Superficie='652090', AñoInde='1919', Poblacion='22720000', EsperanzaVida='45.9', NombreLocal= 'Afganistan/Afqanestan', Gobierno='Islamic Emirate',Presidente='Mohammad Omar')]
list_Pais3 =  [Pais(    Code='AGO', Nombre='Angola', Continente='Africa', Region='Central Africa', Superficie='1246700', AñoInde='1975', Poblacion='12878000', EsperanzaVida='38.3', NombreLocal= 'Angola', Gobierno='Republic',Presidente='José Eduardo dos Santos')]
list_Pais4 =  [Pais(    Code='AIA', Nombre='Anguilla', Continente='North America', Region='Caribbean', Superficie='96', AñoInde='0', Poblacion='8000', EsperanzaVida='76.1', NombreLocal= 'Anguilla', Gobierno='Dependent Territory of the UK',Presidente='Elisabeth II')]
list_Pais5 =  [Pais(    Code='ALB', Nombre='Albania', Continente='Europa', Region='Southern Europe', Superficie='28748', AñoInde='1912', Poblacion='3401200', EsperanzaVida='71.6', NombreLocal= 'Shqiperia', Gobierno='Republic',Presidente='Rexhep Mejdani')]
list_Pais6 =  [Pais(    Code='AND', Nombre='Andorra', Continente='Europa', Region='Southern Europe', Superficie='468', AñoInde='1278', Poblacion='78000', EsperanzaVida='83.5', NombreLocal= 'Andorra', Gobierno='Parliamentary Coprincipality',Presidente='Jacint F. Husson')]
list_Pais7 =  [Pais(    Code='ANT', Nombre='Netherlands Antilles', Continente='North America', Region='Caribbean', Superficie='800', AñoInde='0', Poblacion='217000', EsperanzaVida='74.7', NombreLocal= 'Nederlandse Antillen', Gobierno='Nonmetropolitan Territory of The Netherlands',Presidente='Beatrix')]
list_Pais8 =  [Pais(    Code='ARE', Nombre='United Arab Emirates', Continente='Asia', Region='Middle East', Superficie='83600', AñoInde='1971', Poblacion='2441000', EsperanzaVida='74.1', NombreLocal= 'Al-Imarat al-Arabiya al-Muttahida', Gobierno='Emirate Federation',Presidente='Zayid bin Sultan al-Nahayan')]
list_Pais9 =  [Pais(    Code='ARG', Nombre='Argentina', Continente='South America', Region='South America', Superficie='2780400', AñoInde='1816', Poblacion='37032000', EsperanzaVida='75.1', NombreLocal= 'Argentina', Gobierno='Federal Republic',Presidente='Fernando de la Rúa')]
list_Pais10=  [Pais(    Code='ARM', Nombre='Armenia', Continente='Asia', Region='Middle East', Superficie='29800', AñoInde='1991', Poblacion='3520000', EsperanzaVida='66.4', NombreLocal= 'Hajastan', Gobierno='Republic',Presidente='Robert Kotšarjan')]
list_Pais11 =  [Pais(    Code='ASM', Nombre='American Samoa', Continente='Oceania', Region='Polynesia', Superficie='199', AñoInde='0', Poblacion='68000', EsperanzaVida='75.1', NombreLocal= 'Amerika Samoa', Gobierno='US Territory',Presidente='George W. Bush')]
list_Pais12 =  [Pais(    Code='ATA', Nombre='Antarctica', Continente='Antarctica', Region='Antarctica', Superficie='13120000', AñoInde='0', Poblacion='0', EsperanzaVida='0', NombreLocal= 'Antarctica', Gobierno='Co-Administrated',Presidente='')]
list_Pais13 =  [Pais(    Code='ATF', Nombre='French Southern territories', Continente='Antarctica', Region='Antarctica', Superficie='7780', AñoInde='0', Poblacion='0', EsperanzaVida='0', NombreLocal= 'Terres australes françaises', Gobierno='Nonmetropolitan Territory of France',Presidente='Jacques Chirac')]
list_Pais14 =  [Pais(    Code='ATG', Nombre='Antigua and Barbuda', Continente='North America', Region='Caribbean', Superficie='442', AñoInde='1981', Poblacion='68000', EsperanzaVida='70.5', NombreLocal= 'Antigua and Barbuda', Gobierno='Constitutional Monarchy',Presidente='Elisabeth II')]
list_Pais15 =  [Pais(    Code='AUS', Nombre='Australia', Continente='Oceania', Region='Australia and New Zealand', Superficie='7741220', AñoInde='1901', Poblacion='18886000', EsperanzaVida='79.8', NombreLocal= 'Australia', Gobierno='Constitutional Monarchy, Federation',Presidente='Elisabeth II')]
list_Pais16 =  [Pais(    Code='AUT', Nombre='Austria', Continente='Europe', Region='Western Europe', Superficie='83859', AñoInde='1918', Poblacion='8091800', EsperanzaVida='77.7', NombreLocal= 'Osterreich', Gobierno='Federal Republic',Presidente='Thomas Klestil')]
list_Pais17 =  [Pais(    Code='AZE', Nombre='Azerbaijan', Continente='Asia', Region='Middle East', Superficie='86600', AñoInde='1991', Poblacion='7734000', EsperanzaVida='62.9', NombreLocal= 'Azarbaycan', Gobierno='Federal Republic',Presidente='Heydar aliyev')]
list_Pais18 =  [Pais(    Code='BDI', Nombre='Burundi', Continente='Africa', Region='Eastern Africa', Superficie='27834', AñoInde='1962', Poblacion='6695000', EsperanzaVida='46.2', NombreLocal= 'Burundi\/uburundi', Gobierno='Republic',Presidente='Pierre Buyoya')]
list_Pais19 =  [Pais(    Code='BEL', Nombre='Belgium', Continente='Europe', Region='Western Europe', Superficie='30518', AñoInde='1830', Poblacion='10239000', EsperanzaVida='77.8', NombreLocal= 'Belgie\/Belgique', Gobierno='Constitutional Monarchy, Federation',Presidente='Albert II')]
list_Pais20 =  [Pais(    Code='BEN', Nombre='Benin', Continente='Africa', Region='Western Africa', Superficie='112622', AñoInde='1960', Poblacion='6097000', EsperanzaVida='50.2', NombreLocal= 'Benin', Gobierno='Republic',Presidente='Mathieu Kerekou')]
list_Pais21 =  [Pais(    Code='BFA', Nombre='Burkina Faso', Continente='Africa', Region='Western Africa', Superficie='274000', AñoInde='1960', Poblacion='11937000', EsperanzaVida='46.7', NombreLocal= 'Burkina Faso', Gobierno='Republic',Presidente='Blaise Compaore')]
list_Pais22 =  [Pais(    Code='BGD', Nombre='Bangladesh', Continente='Asia', Region='Southern and Central Asia', Superficie='143998', AñoInde='1971', Poblacion='129155000', EsperanzaVida='60.2', NombreLocal= 'Bangladesh', Gobierno='Constitutional Monarchy',Presidente='Shahabuddin Ahmad')]
list_Pais23 =  [Pais(    Code='BGR', Nombre='Bulgaria', Continente='Europe', Region='Eastern Europe', Superficie='110994', AñoInde='1908', Poblacion='8190900', EsperanzaVida='70.9', NombreLocal= 'Balgarija', Gobierno='Republic',Presidente='Petar Stojanov')]
list_Pais24 =  [Pais(    Code='BHR', Nombre='Bahrain', Continente='Asia', Region='Middle East', Superficie='694', AñoInde='1971', Poblacion='617000', EsperanzaVida='73', NombreLocal= 'Al-Bahrayn', Gobierno='Monarchy (Emirate)',Presidente='Hamad ibn Isa al-Khalifa')]
list_Pais25 =  [Pais(    Code='BHS', Nombre='Bahamas', Continente='North America', Region='Caribbean', Superficie='13878', AñoInde='1973', Poblacion='307000', EsperanzaVida='71.1', NombreLocal= 'The Bahamas', Gobierno='Constitutional Monarchy',Presidente='Elisabeth II')]
list_Pais26 =  [Pais(    Code='BIH', Nombre='Bosnia and Herzegovina', Continente='Europe', Region='Southern Europe', Superficie='51197', AñoInde='1992', Poblacion='3972000', EsperanzaVida='71.5', NombreLocal= 'Bosna i Hercegovina', Gobierno='Federal Republic',Presidente='Ante Jelavic')]
list_Pais27 =  [Pais(    Code='BLR', Nombre='Belarus', Continente='Europe', Region='Eastern Europe', Superficie='207600', AñoInde='1991', Poblacion='10236000', EsperanzaVida='68', NombreLocal= 'Belarus', Gobierno='Republic',Presidente='Aljaksandr LukaSenka')]
list_Pais28 =  [Pais(    Code='BLZ', Nombre='Belize', Continente='North America', Region='Central America', Superficie='22696', AñoInde='1981', Poblacion='241000', EsperanzaVida='70.9', NombreLocal= 'Belize', Gobierno='Constitutional Monarchy',Presidente='Elisabeth II')]
list_Pais29 =  [Pais(    Code='BMU', Nombre='Bermuda', Continente='North America', Region ='North America', Superficie='53', AñoInde='0', Poblacion='65000', EsperanzaVida='76.9', NombreLocal= 'Bermuda', Gobierno='Dependent Territory of the uK',Presidente='Elisabeth II')]
list_Pais30 =  [Pais(    Code='BOL', Nombre='Bolivia', Continente='South America', Region ='South America', Superficie='1098581', AñoInde='1825', Poblacion='8329000', EsperanzaVida='63.7', NombreLocal= 'Bolivia', Gobierno='Republic',Presidente='Hugo Banzer Suarez')]
list_Pais31 =  [Pais(    Code='BRA', Nombre='Brasil', Continente='South America', Region ='South America', Superficie='8547403', AñoInde='1822', Poblacion='170115000', EsperanzaVida=' 62.9', NombreLocal= 'Brasil', Gobierno='Federal Republic',Presidente='Fernando Henrique Cardoso')]
list_Pais32 =  [Pais(    Code='BRB', Nombre='Barbados', Continente='North America', Region ='Caribbean', Superficie='430', AñoInde='1966', Poblacion='270000', EsperanzaVida='73', NombreLocal= 'Barbados', Gobierno='Constitutional Monarchy',Presidente='Elisabeth II')]
list_Pais33 =  [Pais(    Code='BRN', Nombre='Brunei', Continente='Asia', Region ='Southeast Asia', Superficie='5765', AñoInde='1984', Poblacion='328000', EsperanzaVida='73.6', NombreLocal= 'Brunei Darussalam', Gobierno='Monarchy (Sultanate)',Presidente='Haji Hassan al-Bolkiah'),]
list_Pais34 =  [Pais(    Code='BTN', Nombre='Bhutan', Continente='Asia', Region ='Southern and Central Asia', Superficie='47000', AñoInde='1910', Poblacion='2124000', EsperanzaVida='52.4', NombreLocal= 'Druk-Yul', Gobierno='Monarchy',Presidente='Jigme Singye Wangchuk')]
list_Pais35 =  [Pais(    Code='BVT', Nombre='Bouvet Island', Continente='Antarctica', Region ='Antarctica', Superficie='59', AñoInde='0', Poblacion='0', EsperanzaVida='0', NombreLocal= 'Bouvetoya', Gobierno='Dependent Territory of Norway',Presidente='Harald V')]
list_Pais36 =  [Pais(    Code='BWA', Nombre='Botswana', Continente='Africa', Region ='Southern Africa', Superficie='581730', AñoInde='1966', Poblacion='1622000', EsperanzaVida='39.3', NombreLocal= 'Botswana', Gobierno='Republic',Presidente='Festus G. Mogae')]
list_Pais37 =  [Pais(    Code='CAF', Nombre='Central African Republic', Continente='Africa', Region ='Central Africa', Superficie='622984', AñoInde='1960', Poblacion='3615000', EsperanzaVida='44', NombreLocal= 'Centrafrique\/Be-Afrika', Gobierno='Republic',Presidente='Ange-Felix Patasse')]
list_Pais38 =  [Pais(    Code='CAN', Nombre='Canada', Continente='North America', Region ='North America', Superficie='9970610', AñoInde='1867', Poblacion='31147000', EsperanzaVida='79.4', NombreLocal= 'Canada', Gobierno='Constitutional Monarchy, Federation',Presidente='Elisabeth II')]              
list_Pais39 =  [Pais(    Code='CCK', Nombre='Cocos (Keeling) Islands', Continente='Oceania', Region ='Australia and New Zealand', Superficie='14', AñoInde='0', Poblacion='600', EsperanzaVida='0', NombreLocal= 'Cocos (Keeling) Islands', Gobierno='Territory of Australia',Presidente='Elisabeth II'),]                 
list_Pais40 =  [Pais(    Code='CHE', Nombre='Switzerland', Continente='Europe', Region ='Western Europe', Superficie='41284', AñoInde='1499', Poblacion='7160400', EsperanzaVida='79.6', NombreLocal= 'Schweiz\/Suisse\/Svizzera\/Svizra', Gobierno='Federation',Presidente='Adolf Ogi')]               
list_Pais41 =  [Pais(    Code='CHL', Nombre='Chile', Continente='South America', Region ='South America', Superficie='756626', AñoInde='1810', Poblacion='15211000', EsperanzaVida='75.7', NombreLocal= 'Chile', Gobierno='Republic',Presidente='Ricardo Lagos Escobar')] 
list_Pais42 =  [Pais(    Code='CHN', Nombre='China', Continente='Asia', Region ='Eastern Asia', Superficie='9572900', AñoInde='-1523', Poblacion='1277558000', EsperanzaVida='71.4', NombreLocal= 'Zhongquo', Gobierno='People Republic',Presidente='Jiang Zemin')]         
list_Pais43 =  [Pais(    Code='CIV', Nombre='Cote dIvoire', Continente='Africa', Region ='Western Africa', Superficie='322463', AñoInde='1960', Poblacion='14786000', EsperanzaVida='45.2', NombreLocal= 'Cote dIvoire', Gobierno='Republic',Presidente='Laurent Gbagbo')]
list_Pais44 =  [Pais(    Code='CMR', Nombre='Cameroon', Continente='Africa', Region ='Central Africa', Superficie='475442', AñoInde='1960', Poblacion='15085000', EsperanzaVida='54.8', NombreLocal= 'Cameroun\/Cameroon', Gobierno='Republic',Presidente='Paul Biya')]        
list_Pais45 =  [Pais(    Code='COD', Nombre='Congo, The Democratic Republic of the', Continente='Africa', Region ='Central Africa', Superficie='2344858', AñoInde='1960', Poblacion='2344858', EsperanzaVida='48.8', NombreLocal= 'Republique Democratique du Congo', Gobierno='Republic',Presidente='Joseph Kabila')]  
list_Pais46 =  [Pais(    Code='COG', Nombre='Congo', Continente='Africa', Region ='Central Africa', Superficie='342000', AñoInde='1960', Poblacion='2943000', EsperanzaVida='47.4', NombreLocal= 'Congo', Gobierno='Republic',Presidente='Denis Sassou-Nguesso')]
list_Pais47 =  [Pais(    Code='COK', Nombre='Cook Islands', Continente='Oceania', Region ='Polynesia', Superficie='236', AñoInde='0', Poblacion='20000', EsperanzaVida='71.1', NombreLocal= 'The Cook Islands', Gobierno='Nonmetropolitan Territory of New Zealand',Presidente='Elisabeth II')]
list_Pais48 =  [Pais(    Code='COL', Nombre='Colombia', Continente='South America', Region ='South America', Superficie='1138914', AñoInde='1810', Poblacion='42321000', EsperanzaVida='70.3', NombreLocal= 'Colombia', Gobierno='Republic',Presidente='Andres Pastrana Arango')]            
list_Pais49 =  [Pais(    Code='COM', Nombre='Comoros', Continente='Africa', Region ='Eastern Africa', Superficie='1862', AñoInde='1975', Poblacion='578000', EsperanzaVida='60', NombreLocal= 'Komori\/Comores', Gobierno='Republic',Presidente='Azali Assoumani')]
list_Pais50 =  [Pais(    Code='CPV', Nombre='Cape Verde', Continente='Africa', Region ='Western Africa', Superficie='4033', AñoInde='1975', Poblacion='428000', EsperanzaVida='68.9', NombreLocal= 'Cabo Verde', Gobierno='Republic',Presidente='Antonio Mascarenhas Monteiro')]
list_Pais51 =  [Pais(    Code='CRI', Nombre='Costa Rica', Continente='North America', Region ='Central America', Superficie='51100', AñoInde='1821', Poblacion='4023000', EsperanzaVida='75.8', NombreLocal= 'Costa Rica', Gobierno='Republic',Presidente='Miguel angel RodrIguez EcheverrIa')]                                    
list_Pais52 =  [Pais(    Code='CUB', Nombre='Cuba', Continente='North America', Region ='Caribbean', Superficie='110861', AñoInde='1902', Poblacion='11201000', EsperanzaVida='76.2', NombreLocal= 'Cuba', Gobierno='Socialistic Republic',Presidente='Fidel Castro Ruz')]   
list_Pais53 =  [Pais(    Code='CXR', Nombre='Christmas Island', Continente='Oceania', Region ='Australia and New Zealand', Superficie='135', AñoInde='0', Poblacion='2500', EsperanzaVida='0', NombreLocal= 'Christmas Island', Gobierno='Territory of Australia',Presidente='Elisabeth II')]  
list_Pais54 =  [Pais(    Code='CYP', Nombre='Cyprus', Continente='Asia', Region ='Middle East', Superficie='9251', AñoInde='1960', Poblacion='754700', EsperanzaVida='76.7', NombreLocal= 'Kypros\/Kibris', Gobierno='Republic',Presidente='Glafkos Klerides')]
list_Pais55 =  [Pais(    Code='CYM', Nombre='Cayman Islands', Continente='North America', Region ='Caribbean', Superficie='264', AñoInde='0', Poblacion='38000', EsperanzaVida='78.9', NombreLocal= 'Cayman Islands', Gobierno='Dependent Territory of the uK',Presidente='Elisabeth II')]
list_Pais56 =  [Pais(    Code='CZE', Nombre='Czech Republic', Continente='Europe', Region ='Eastern Europe', Superficie='78866', AñoInde='1993', Poblacion='10278100', EsperanzaVida='78.9', NombreLocal= 'Cayman Islands', Gobierno='Dependent Territory of the uK',Presidente='Elisabeth II')]
list_Pais57 =  [Pais(    Code='DEU', Nombre='Germany', Continente='Europe', Region ='Western Europe', Superficie='357022', AñoInde='1955', Poblacion='82164700', EsperanzaVida='77.4', NombreLocal= 'Deutschland', Gobierno='Federal Republic',Presidente='Johannes Rau')]
list_Pais58 =  [Pais(    Code='DJI', Nombre='Djibouti', Continente='Africa', Region ='Eastern Africa', Superficie='23200', AñoInde='1977', Poblacion='638000', EsperanzaVida='50.8', NombreLocal= 'Djibouti\/Jibuti', Gobierno='Republic',Presidente='Ismail Omar Guelleh')]                     
list_Pais59 =  [Pais(    Code='DMA', Nombre='Dominica', Continente='North America', Region ='Eastern Africa', Superficie='751', AñoInde='1978', Poblacion='7100', EsperanzaVida='73.4', NombreLocal='Dominica', Gobierno='Republic',Presidente='Vernon Shaw')]
list_Pais60 =  [Pais(    Code='DNK', Nombre='Denmark', Continente='Europe', Region ='Nordic Countries', Superficie='43094', AñoInde='800', Poblacion='5330000', EsperanzaVida='76.5', NombreLocal='Danmark', Gobierno='Constitutional Monarchy',Presidente='Margrethe II')]
list_Pais61 =  [Pais(    Code='DOM', Nombre='Dominican Republic', Continente='North America', Region ='Caribbean', Superficie='48511', AñoInde='1844', Poblacion='8495000', EsperanzaVida='73.2', NombreLocal='Republica Dominicana', Gobierno='Republic',Presidente='Hipolito MejIa DomInguez')]
list_Pais62 =  [Pais(    Code='DZA', Nombre='Algeria', Continente='Northern Africa', Region ='Caribbean', Superficie='2381741', AñoInde='1962', Poblacion='31471000', EsperanzaVida='69.7', NombreLocal='Al-Jazair\/Algerie', Gobierno='Republic',Presidente='Abdelaziz Bouteflika')] 
list_Pais63 =  [Pais(    Code='ECU', Nombre='Ecuador', Continente='South America', Region ='South America', Superficie='283561', AñoInde='1822', Poblacion='12646000', EsperanzaVida='71.1', NombreLocal='Ecuador', Gobierno='Republic',Presidente='Gustavo Noboa Bejarano')]  
list_Pais64 =  [Pais(    Code='EGY', Nombre='Egypt', Continente='Africa', Region ='Northern Africa', Superficie='1001449', AñoInde='1922', Poblacion='68470000', EsperanzaVida='63.3', NombreLocal='Misr', Gobierno='Republic',Presidente='Hosni Mubarak')]
list_Pais65 =  [Pais(    Code='ERI', Nombre='Eritrea', Continente='Africa', Region ='Eastern Africa', Superficie='117600', AñoInde='1993', Poblacion='3850000', EsperanzaVida='55.8', NombreLocal='Ertra', Gobierno='Republic',Presidente='Isayas Afewerki [Isaias Afwerki]')]  
list_Pais66 =  [Pais(    Code='ESH', Nombre='Western Sahara', Continente='Africa', Region ='Northern Africa', Superficie='266000', AñoInde='0', Poblacion='293000', EsperanzaVida='49.8', NombreLocal='As-Sahrawiya', Gobierno='As-Sahrawiya',Presidente='Mohammed Abdel Aziz')]
list_Pais67 =  [Pais(    Code='ESP', Nombre='Spain', Continente='Europe', Region ='Southern Europe', Superficie='505992', AñoInde='1492', Poblacion='39441700', EsperanzaVida=' 78.8', NombreLocal='Espana', Gobierno='Constitutional Monarchy',Presidente='Juan Carlos I')]
list_Pais68 =  [Pais(    Code='EST', Nombre='Estonia', Continente='Europe', Region ='Baltic Countries', Superficie='45227', AñoInde='1991', Poblacion='1439200', EsperanzaVida=' 69.5', NombreLocal='Eesti', Gobierno='Republic',Presidente='Lennart Meri')]
list_Pais69 =  [Pais(    Code='ETH', Nombre='Ethiopia', Continente='Africa', Region ='Eastern Africa', Superficie='1104300', AñoInde='-1000', Poblacion='62565000', EsperanzaVida='45.2', NombreLocal='YeItyop iya', Gobierno='Republic',Presidente='Negasso Gidada')]
list_Pais70 =  [Pais(    Code='FIN', Nombre='Finland', Continente='Europe', Region ='Nordic Countries', Superficie='338145', AñoInde='1917', Poblacion='5171300', EsperanzaVida='77.4', NombreLocal='Suomi', Gobierno='Republic',Presidente='Tarja Halonen')]
list_Pais71 =  [Pais(    Code='FJI', Nombre='Fiji Islands', Continente='Oceania', Region ='Melanesia', Superficie='18274', AñoInde='1970', Poblacion='817000', EsperanzaVida='67.9', NombreLocal='Fiji Islands', Gobierno='Republic',Presidente='Josefa Iloilo')]  
list_Pais72 =  [Pais(    Code = 'FLK', Nombre =  'Falkland Islands', Continente= 'South America', Region = 'South America', Superficie= '12173', AñoInde =  '0',Poblacion =  '2000', EsperanzaVida ='0', NombreLocal = 'Falkland Islands', Gobierno = 'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais73 =  [Pais(    Code= 'FRA', Nombre =  'France', Continente= 'Europe', Region = 'Western Europe', Superficie= '551500', AñoInde =  '843', Poblacion = '59225700', EsperanzaVida = '78.8', NombreLocal = 'France', Gobierno = 'Republic', Presidente= 'Jacques Chirac')]
list_Pais74 =  [Pais(    Code= 'FRO', Nombre =  'Faroe Islands', Continente= 'Europe', Region = 'Nordic Countries', Superficie= '1399', AñoInde =  '0', Poblacion =  '43000', EsperanzaVida =  '78.4', NombreLocal = 'Foroyar', Gobierno = 'Part of Denmark', Presidente= 'Margrethe II')]
list_Pais75 =  [Pais(    Code= 'FSM',Nombre =  'Micronesia, Federated States of', Continente= 'Oceania', Region = 'Micronesia', Superficie= '702', AñoInde =  '1990', Poblacion =  '119000', EsperanzaVida = '68.6', NombreLocal = 'Micronesia', Gobierno = 'Federal Republic', Presidente= 'Leo A. Falcam')]
list_Pais76 =  [Pais(    Code= 'GAB', Nombre =  'Gabon',Continente= 'Africa', Region = 'Central Africa', Superficie= '267668', AñoInde =  '1960', Poblacion =  '1226000', EsperanzaVida = '50.1', NombreLocal = 'Le Gabon',Gobierno = 'Republic', Presidente= 'Omar Bongo')]
list_Pais77 =  [Pais(    Code= 'GBR', Nombre =  'united Kingdom', Continente= 'Europe', Region = 'British Islands', Superficie= '242900', AñoInde =  '1066', Poblacion =  '59623400', EsperanzaVida = '77.7', NombreLocal = 'united Kingdom', Gobierno = 'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais78 =  [Pais(    Code= 'GEO', Nombre =  'Georgia', Continente= 'Asia', Region = 'Middle East', Superficie= '69700', AñoInde =  '1991', Poblacion =  '4968000',  EsperanzaVida = '64.5', NombreLocal = 'Sakartvelo', Gobierno = 'Republic', Presidente= 'Eduard Sevardnadze' )]          
list_Pais79 =  [Pais(    Code= 'GHA', Nombre =  'Ghana', Continente= 'Africa', Region = 'Western Africa', Superficie= '238533', AñoInde =  '1957', Poblacion =  '20212000', EsperanzaVida = '57.4', NombreLocal = 'Ghana', Gobierno = 'Republic', Presidente= 'John Kufuor')]
list_Pais80 =  [Pais(    Code= 'GIB', Nombre =  'Gibraltar', Continente= 'Europe', Region = 'Southern Europe', Superficie= '6', AñoInde =  '0', Poblacion =  '25000', EsperanzaVida =  '79', NombreLocal = 'Gibraltar', Gobierno = 'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais81 =  [Pais(    Code= 'GIN', Nombre =  'Guinea', Continente= 'Africa', Region = 'Western Africa', Superficie= '245857', AñoInde =  '1958', Poblacion =  '7430000', EsperanzaVida = '45.6', NombreLocal = 'Guinee', Gobierno = 'Republic', Presidente= 'Lansana Conte')]
list_Pais82 =  [Pais(    Code= 'GLP', Nombre =  'Guadeloupe', Continente= 'North America', Region = 'Caribbean', Superficie= '1705',AñoInde =  '0', Poblacion =  '456000', EsperanzaVida = '77', NombreLocal = 'Guadeloupe', Gobierno = 'Overseas Department of France', Presidente= 'Jacques Chirac')]
list_Pais83 =  [Pais(    Code= 'GMB', Nombre =  'Gambia', Continente= 'Africa', Region = 'Western Africa', Superficie= '11295', AñoInde =  '1965', Poblacion =  '1305000', EsperanzaVida = '53.2', NombreLocal = 'The Gambia', Gobierno = 'Republic', Presidente= 'Yahya Jammeh')]
list_Pais84 =  [Pais(    Code= 'GNB', Nombre =  'Guinea-Bissau', Continente= 'Africa', Region = 'Western Africa', Superficie= '36125', AñoInde =  '1974', Poblacion =  '1213000', EsperanzaVida = '49',  NombreLocal = 'Guine-Bissau', Gobierno = 'Republic', Presidente= 'Kumba Iala')]
list_Pais85 =  [Pais(    Code= 'GNQ',  Nombre =  'Equatorial Guinea', Continente= 'Africa', Region = 'Central Africa', Superficie= '28051', AñoInde =  '1968', Poblacion =  '453000', EsperanzaVida = '53.6', NombreLocal = 'Guinea Ecuatorial', Gobierno = 'Republic', Presidente= 'Teodoro Obiang Nguema Mbasogo')]
list_Pais86 =  [Pais(    Code= 'GRC', Nombre =  'Greece', Continente= 'Europe',Region = 'Southern Europe', Superficie='131626', AñoInde =  '1830', Poblacion =  '10545700', EsperanzaVida = '78.4', NombreLocal = 'Ellada', Gobierno = 'Republic', Presidente= 'Kostis Stefanopoulos')]
list_Pais87 =  [Pais(    Code= 'GRD', Nombre =  'Grenada', Continente= 'North America', Region = 'Caribbean', Superficie= '344', AñoInde =  '1974', Poblacion =  '94000', EsperanzaVida =   '64.5', NombreLocal = 'Grenada', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais88 =  [Pais(    Code= 'GRL', Nombre =  'Greenland', Continente= 'North America', Region = 'North America', Superficie= '2166090', AñoInde =  '0', Poblacion =  '56000', EsperanzaVida =   '68.1', NombreLocal = 'Kalaallit Nunaat\/Gronland', Gobierno =  'Part of Denmark', Presidente= 'Margrethe II')]
list_Pais89 =  [Pais(    Code= 'GTM', Nombre =  'Guatemala', Continente= 'North America', Region = 'Central America', Superficie= '108889', AñoInde =  '1821', Poblacion =  '11385000', EsperanzaVida =   '66.2', NombreLocal = 'Guatemala', Gobierno =  'Republic', Presidente= 'Alfonso Portillo Cabrera')]
list_Pais90 =  [Pais(    Code= 'GUF', Nombre =  'French Guiana', Continente= 'South America', Region = 'South America', Superficie= '90000', AñoInde =  '0', Poblacion =  '181000', EsperanzaVida =   '76.1', NombreLocal = 'Guyane francaise', Gobierno =  'Overseas Department of France', Presidente= 'Jacques Chirac')]
list_Pais91 =  [Pais(    Code= 'GUM', Nombre =  'Guam', Continente= 'Oceania', Region = 'Micronesia', Superficie= '549', AñoInde =  '0', Poblacion =  '168000', EsperanzaVida =   '77.8', NombreLocal = 'Guam', Gobierno =  'uS Territory', Presidente= 'George W. Bush')]
list_Pais92 =  [Pais(    Code= 'GUY', Nombre =  'Guyana',Continente= 'South America',Region = 'South America', Superficie= '214969',AñoInde =  '1966',Poblacion =  '861000', EsperanzaVida =   '64', NombreLocal = 'Guyana', Gobierno =  'Republic', Presidente= 'Bharrat Jagdeo')]
list_Pais93 =  [Pais(    Code= 'HKG', Nombre =  'Hong Kong', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '1075', AñoInde =  '0', Poblacion =  '6782000', EsperanzaVida =   '79.5', NombreLocal = 'Xianggang\/Hong Kong', Gobierno =  'Special Administrative Region of China', Presidente= 'Jiang Zemin')]
list_Pais94 =  [Pais(    Code= 'HMD', Nombre =  'Heard Island and McDonald Islands', Continente= 'Antarctica', Region = 'Antarctica', Superficie= '359', AñoInde =  '0', Poblacion =  '0', EsperanzaVida =   '0', NombreLocal = 'Heard and McDonald Islands', Gobierno =  'Territory of Australia', Presidente= 'Elisabeth II')]
list_Pais95 =  [Pais(    Code= 'HND', Nombre =  'Honduras', Continente= 'North America', Region = 'Central America', Superficie= '112088', AñoInde =  '1838', Poblacion =  '6485000', EsperanzaVida =   '69.9', NombreLocal = 'Honduras', Gobierno =  'Republic',Presidente= 'Carlos Roberto Flores Facusse')]
list_Pais96 =  [Pais(    Code= 'HRV', Nombre =  'Croatia', Continente= 'Europe', Region = 'Southern Europe', Superficie= '56538', AñoInde =  '1991', Poblacion = '4473000', EsperanzaVida =   '73.7', NombreLocal = 'Hrvatska', Gobierno =  'Republic', Presidente= 'Stipe Mesic')]
list_Pais97 =  [Pais(    Code= 'HTI', Nombre =  'Haiti', Continente= 'North America', Region = 'Caribbean', Superficie= '27750', AñoInde =  '1804', Poblacion =  '222000', EsperanzaVida =   '49.2', NombreLocal = 'Haiti\/Dayti', Gobierno =  'Republic', Presidente= 'Jean-Bertrand Aristide')]
list_Pais98 =  [Pais(    Code= 'HUN', Nombre =  'Hungary', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '93030', AñoInde =  '1918', Poblacion =  '10043200', EsperanzaVida =   '71.4', NombreLocal = 'Magyarorszag', Gobierno =  'Republic', Presidente= 'Ferenc Madl')]
list_Pais99 =  [Pais(    Code= 'IDN', Nombre =  'Indonesia', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '1904569', AñoInde =  '1945', Poblacion =  '212107000', EsperanzaVida =   '68', NombreLocal = 'Indonesia', Gobierno =  'Republic', Presidente= 'Abdurrahman Wahid')]
list_Pais100 =  [Pais(    Code= 'IND', Nombre =  'India', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '3287263', AñoInde =  '1947', Poblacion =  '1013662000', EsperanzaVida =   '62.5', NombreLocal = 'Bharat\/India', Gobierno =  'Federal Republic', Presidente= 'Kocheril Raman Narayanan')]
list_Pais101 =  [Pais(    Code= 'IOT', Nombre =  'British Indian Ocean Territory', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '78', AñoInde =  '0', Poblacion =  '0', EsperanzaVida =   '0', NombreLocal = 'British Indian Ocean Territory', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais102 =  [Pais(    Code= 'IRL', Nombre =  'Ireland', Continente= 'Europe', Region = 'British Islands', Superficie= '70273', AñoInde =  '1921', Poblacion =  '3775100', EsperanzaVida =   '76.8', NombreLocal = 'Ireland\/eire', Gobierno =  'Republic', Presidente= 'Mary McAleese')]
list_Pais103 =  [Pais(    Code= 'IRN', Nombre =  'Iran', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '1648195', AñoInde =  '1906', Poblacion =  '7702000', EsperanzaVida =   '69.7',  NombreLocal = 'Iran', Gobierno =  'Islamic Republic', Presidente= 'Ali Mohammad Khatami-Ardakani')]
list_Pais104 =  [Pais(    Code= 'IRQ', Nombre =  'Iraq', Continente= 'Asia', Region = 'Middle East', Superficie= '438317', AñoInde =  '1932', Poblacion =  '23115000', EsperanzaVida =   '66.5', NombreLocal = 'Al- Iraq', Gobierno =  'Republic', Presidente= 'Saddam Hussein al-Takriti')]
list_Pais105 =  [Pais(    Code= 'ISL', Nombre =  'Iceland', Continente= 'Europe', Region = 'Nordic Countries', Superficie= '103000', AñoInde =  '1944', Poblacion =  '279000', EsperanzaVida =   '79.4', NombreLocal = 'Island',Gobierno =  'Republic', Presidente= 'olafur Ragnar GrImsson')]
list_Pais106 =  [Pais(    Code= 'ISR',  Nombre =  'Israel', Continente= 'Asia', Region = 'Middle East', Superficie= '21056', AñoInde =  '1948', Poblacion =  '6217000', EsperanzaVida =   '78.6', NombreLocal = 'Yisrael\/Israil', Gobierno =  'Republic', Presidente= 'Moshe Katzav')]
list_Pais107 =  [Pais(    Code= 'ITA', Nombre =  'Italy', Continente= 'Europe', Region = 'Southern Europe', Superficie= '3013160', AñoInde =  '1861', Poblacion =  '57680000', EsperanzaVida =   '79', NombreLocal = 'Italia', Gobierno =  'Republic', Presidente= 'Carlo Azeglio Ciampi')]
list_Pais108 =  [Pais(    Code= 'JAM', Nombre =  'Jamaica', Continente= 'North America', Region = 'Caribbean', Superficie= '10990', AñoInde =  '1962', Poblacion =  '2583000', EsperanzaVida =   '75.2', NombreLocal = 'Jamaica', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais109 =  [Pais(    Code= 'JOR', Nombre =  'Jordan', Continente= 'Asia', Region = 'Middle East', Superficie= '88946', AñoInde =  '1946', Poblacion =  '5083000', EsperanzaVida =   '77.4', NombreLocal = 'Al-urdunn', Gobierno =  'Constitutional Monarchy', Presidente= 'Abdullah II')]
list_Pais110 =  [Pais(    Code= 'JPN', Nombre =  'Japan', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '377829', AñoInde =  '-660', Poblacion =  '126714000', EsperanzaVida =   '80.7',NombreLocal = 'Nihon\/Nippon', Gobierno =  'Constitutional Monarchy', Presidente= 'Akihito')]
list_Pais111 =  [Pais(    Code= 'KAZ', Nombre =  'Kazakstan', Continente= 'Asia',Region = 'Southern and Central Asia', Superficie= '2724900', AñoInde =  '1991', Poblacion =  '16223000', EsperanzaVida =   '63.2', NombreLocal = 'Qazaqstan', Gobierno =  'Republic',Presidente= 'Nursultan Nazarbajev')]
list_Pais112 =  [Pais(    Code= 'KEN', Nombre =  'Kenya', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '580367', AñoInde =  '1963', Poblacion =  '30080000', EsperanzaVida =   '48', NombreLocal = 'Kenya', Gobierno =  'Republic', Presidente= 'Daniel arap Moi')]
list_Pais113 =  [Pais(    Code= 'KGZ', Nombre =  'Kyrgyzstan', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '199900', AñoInde =  '1991', Poblacion =  '4699000', EsperanzaVida =   '63.4', NombreLocal = 'Kyrgyzstan', Gobierno =  'Republic', Presidente= 'Askar Akajev')]
list_Pais114 =  [Pais(    Code= 'KHM', Nombre =  'Cambodia', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '181035', AñoInde =  '1953', Poblacion =  '11168000', EsperanzaVida =   '56.5', NombreLocal = 'Kampuchea', Gobierno =  'Constitutional Monarchy', Presidente= 'Norodom Sihanouk')]
list_Pais115 =  [Pais(    Code= 'KIR', Nombre =  'Kiribati', Continente= 'Oceania', Region = 'Micronesia', Superficie= '726', AñoInde =  '1979', Poblacion =  '83000', EsperanzaVida =   '59.8', NombreLocal = 'Kiribati',Gobierno =  'Republic', Presidente= 'Teburoro Tito')]
list_Pais116 =  [Pais(    Code= 'KNA', Nombre =  'Saint Kitts and Nevis',Continente= 'North America', Region = 'Caribbean', Superficie= '261', AñoInde =  '1983', Poblacion =  '38000', EsperanzaVida =   '70.7', NombreLocal = 'Saint Kitts and Nevis', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais117 =  [Pais(    Code= 'KOR', Nombre =  'South Korea', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '99434', AñoInde =  '1948', Poblacion =  '46844000', EsperanzaVida =   '74.4', NombreLocal = 'Taehan Minguk (Namhan)', Gobierno =  'Republic', Presidente= 'Kim Dae-jung')]
list_Pais118 =  [Pais(    Code= 'KWT', Nombre =  'Kuwait', Continente= 'Asia', Region = 'Middle East', Superficie= '17818', AñoInde =  '1961', Poblacion =  '1972000', EsperanzaVida =   '76.1', NombreLocal = 'Al-Kuwayt',Gobierno =  'Constitutional Monarchy (Emirate)', Presidente= 'Jabir al-Ahmad al-Jabir al-Sabah')]
list_Pais119 =  [Pais(    Code= 'LAO', Nombre =  'Laos', Continente= 'Asia',Region = 'Southeast Asia', Superficie= '236800',AñoInde =  '1953', Poblacion =  '5433000', EsperanzaVida =   '53.1', NombreLocal = 'Lao', Gobierno =  'Republic', Presidente= 'Khamtay Siphandone')]
list_Pais120 =  [Pais(    Code= 'LBN', Nombre =  'Lebanon', Continente= 'Asia', Region = 'Middle East', Superficie= '10400', AñoInde =  '1941', Poblacion =  '3282000',EsperanzaVida =   '71.3', NombreLocal = 'Lubnan', Gobierno =  'Republic', Presidente= 'emile Lahoud')]
list_Pais121 =  [Pais(    Code= 'LBR', Nombre =  'Liberia', Continente= 'Africa', Region = 'Western Africa', Superficie= '111369', AñoInde =  '1847', Poblacion =  '3154000', EsperanzaVida =   '51', NombreLocal = 'Liberia', Gobierno =  'Republic', Presidente= 'Charles Taylor')]
list_Pais122 =  [Pais(    Code= 'LBY', Nombre =  'Libyan Arab Jamahiriya', Continente= 'Africa', Region = 'Northern Africa', Superficie= '1759540', AñoInde =  '1951', Poblacion =  '5605000', EsperanzaVida =   '75.5', NombreLocal = 'Libiya', Gobierno =  'Socialistic State', Presidente= 'Muammar al-Qadhafi')]
list_Pais123 =  [Pais(    Code= 'LCA', Nombre =  'Saint Lucia', Continente= 'North America', Region = 'Caribbean', Superficie= '622', AñoInde =  '1979', Poblacion =  '154000', EsperanzaVida =   '72.3', NombreLocal = 'Saint Lucia', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais124 =  [Pais(    Code= 'LIE', Nombre =  'Liechtenstein', Continente= 'Europe', Region = 'Western Europe', Superficie= '160', AñoInde =  '1806', Poblacion =  '32300', EsperanzaVida =   '78.8', NombreLocal = 'Liechtenstein', Gobierno =  'Constitutional Monarchy', Presidente= 'Hans-Adam II')]
list_Pais125 =  [Pais(    Code= 'LKA', Nombre =  'Sri Lanka', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '65610', AñoInde =  '1948', Poblacion =  '18827000', EsperanzaVida =   '71.8', NombreLocal = 'Sri Lanka\/Ilankai', Gobierno =  'Republic', Presidente= 'Chandrika Kumaratunga')]
list_Pais126 =  [Pais(    Code= 'LSO', Nombre =  'Lesotho', Continente= 'Africa', Region = 'Southern Africa', Superficie= '30355', AñoInde =  '1966', Poblacion =  '2153000', EsperanzaVida =   '50.8', NombreLocal = 'Lesotho',Gobierno =  'Constitutional Monarchy', Presidente= 'Letsie III')]
list_Pais127 =  [Pais(    Code= 'LTU', Nombre =  'Lithuania', Continente= 'Europe', Region = 'Baltic Countries', Superficie= '65301', AñoInde =  '1991', Poblacion =  '3698500', EsperanzaVida =   '69.1', NombreLocal = 'Lietuva', Gobierno =  'Republic', Presidente= 'Valdas Adamkus')]
list_Pais128 =  [Pais(    Code= 'LUX', Nombre =  'Luxembourg', Continente= 'Europe', Region = 'Western Europe',  Superficie= '2586', AñoInde =  '1867',Poblacion =  '435700',EsperanzaVida =   '77.1', NombreLocal = 'Luxembourg\/Letzebuerg' ,Gobierno =  'Constitutional Monarchy', Presidente= 'Henri')]
list_Pais129 =  [Pais(    Code= 'LVA', Nombre =  'Latvia', Continente= 'Europe', Region = 'Baltic Countries', Superficie= '64589', AñoInde =  '1991', Poblacion =  '2424200', EsperanzaVida =   '68.4', NombreLocal = 'Latvija', Gobierno =  'Republic', Presidente= 'Vaira Vike-Freiberga')]
list_Pais130 =  [Pais(    Code= 'MAC', Nombre =  'Macao', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '18', AñoInde =  '0', Poblacion =  '473000', EsperanzaVida =   '81.6', NombreLocal = 'Macau\/Aomen', Gobierno =  'Special Administrative Region of China', Presidente= 'Jiang Zemin')]
list_Pais131 =  [Pais(    Code= 'MAR', Nombre =  'Morocco', Continente= 'Africa', Region = 'Northern Africa', Superficie= '446550', AñoInde =  '1956', Poblacion =  '28351000', EsperanzaVida =   '69.1', NombreLocal = 'Al-Maghrib', Gobierno =  'Constitutional Monarchy', Presidente= 'Mohammed VI')]
list_Pais132 =  [Pais(    Code= 'MCO', Nombre =  'Monaco', Continente= 'Europe', Region = 'Western Europe', Superficie= '1', AñoInde =  '1861', Poblacion =  '34000', EsperanzaVida =   '78.8', NombreLocal = 'Monaco', Gobierno =  'Constitutional Monarchy', Presidente= 'Rainier III')]
list_Pais133 =  [Pais(    Code= 'MDA', Nombre =  'Moldova', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '33851', AñoInde =  '1991', Poblacion =  '4380000', EsperanzaVida =   '64.5', NombreLocal = 'Moldova', Gobierno =  'Republic', Presidente= 'Vladimir Voronin')]
list_Pais134 =  [Pais(    Code= 'MDG', Nombre =  'Madagascar', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '587041', AñoInde =  '1960', Poblacion =  '15942000', EsperanzaVida =   '55', NombreLocal = 'Madagasikara\/Madagascar', Gobierno =  'Federal Republic', Presidente= 'Didier Ratsiraka')]
list_Pais135 =  [Pais(    Code= 'MDV', Nombre =  'Maldives', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '298', AñoInde =  '1965', Poblacion =  '286000', EsperanzaVida =   '62.2', NombreLocal = 'Dhivehi Raajje\/Maldives', Gobierno =  'Republic', Presidente= 'Maumoon Abdul Gayoom')]
list_Pais136 =  [Pais(    Code= 'MEX', Nombre =  'Mexico', Continente= 'North America', Region = 'Central America', Superficie= '1958201', AñoInde =  '1810', Poblacion =  '98881000', EsperanzaVida =   '71.5',  NombreLocal = 'Mexico', Gobierno =  'Federal Republic', Presidente= 'Vicente Fox Quesada')]
list_Pais137 =  [Pais(    Code= 'MHL', Nombre =  'Marshall Islands', Continente= 'Oceania', Region = 'Micronesia', Superficie= '181', AñoInde =  '1990', Poblacion =  '64000', EsperanzaVida =  '65.5', NombreLocal = 'Marshall Islands\/Majol', Gobierno =  'Republic', Presidente= 'Kessai Note')]
list_Pais138 =  [Pais(    Code= 'MKD', Nombre =  'Macedonia', Continente= 'Europe', Region = 'Southern Europe', Superficie= '25713', AñoInde = '1991',  Poblacion =  '2024000', EsperanzaVida =   '73.8', NombreLocal = 'Makedonija', Gobierno =  'Republic', Presidente= 'Boris Trajkovski')]
list_Pais139 =  [Pais(    Code= 'MLI', Nombre =  'Mali', Continente= 'Africa', Region = 'Western Africa', Superficie= '1240192', AñoInde =  '1960', Poblacion =  '11234000', EsperanzaVida =   '46.7', NombreLocal = 'Mali', Gobierno =  'Republic', Presidente= 'Alpha Oumar Konare')]
list_Pais140 =  [Pais(    Code= 'MLT', Nombre =  'Malta', Continente= 'Europe', Region = 'Southern Europe', Superficie= '316', AñoInde =  '1964', Poblacion =  '380200', EsperanzaVida =   '77.9', NombreLocal = 'Malta', Gobierno =  'Republic', Presidente= 'Guido de Marco')]
list_Pais141 =  [Pais(    Code= 'MMR', Nombre =  'Myanmar', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '676578', AñoInde =  '1948', Poblacion =  '45611000', EsperanzaVida =   '54.9',  NombreLocal = 'Myanma Pye',   Gobierno =  'Republic',Presidente= 'kenraali Than Shwe')]
list_Pais142 =  [Pais(    Code= 'MNG', Nombre =  'Mongolia', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '1566500', AñoInde =  '1921', Poblacion =  '2662000', EsperanzaVida =   '67.3', NombreLocal = 'Mongol uls', Gobierno =  'Republic', Presidente= 'Natsagiin Bagabandi')]
list_Pais143 =  [Pais(    Code= 'MNP', Nombre =  'Northern Mariana Islands', Continente= 'Oceania', Region = 'Micronesia', Superficie= '464', AñoInde =  '0', Poblacion =  '78000', EsperanzaVida =   '75.5', NombreLocal = 'Northern Mariana Islands', Gobierno =  'Commonwealth of the uS', Presidente= 'George W. Bush')]
list_Pais144 =  [Pais(    Code= 'MOZ',Nombre =  'Mozambique', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '801590', AñoInde =  '1975', Poblacion =  '19680000', EsperanzaVida =   '37.5', NombreLocal = 'Mocambique', Gobierno =  'Republic', Presidente= 'JoaquIm A. Chissano')]
list_Pais145 =  [Pais(    Code= 'MRT', Nombre =  'Mauritania', Continente= 'Africa', Region = 'Western Africa', Superficie= '1025520', AñoInde =  '1960', Poblacion =  '2670000', EsperanzaVida =   '50.8', NombreLocal = 'Muritaniya\/Mauritanie', Gobierno =  'Republic', Presidente= 'Maaouiya Ould Sid Ahmad Taya')]
list_Pais146 =  [Pais(    Code= 'MSR', Nombre =  'Montserrat', Continente= 'North America', Region = 'Caribbean', Superficie= '102', AñoInde =  '0', Poblacion =  '11000', EsperanzaVida =   '78', NombreLocal = 'Montserrat', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais147 =  [Pais(    Code= 'MTQ', Nombre =  'Martinique', Continente= 'North America', Region = 'Caribbean', Superficie= '1102', AñoInde =  '0', Poblacion =  '395000', EsperanzaVida =   '78.3', NombreLocal = 'Martinique', Gobierno =  'Overseas Department of France', Presidente= 'Jacques Chirac')]
list_Pais148 =  [Pais(    Code= 'MUS',Nombre =  'Mauritius', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '2040', AñoInde =  '1968', Poblacion =  '1158000', EsperanzaVida =   '71', NombreLocal = 'Mauritius', Gobierno =  'Republic', Presidente= 'Cassam uteem')]
list_Pais149 =  [Pais(    Code= 'MWI', Nombre =  'Malawi', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '118484', AñoInde =  '1964', Poblacion =  '10925000', EsperanzaVida =   '37.6', NombreLocal = 'Malawi', Gobierno =  'Republic', Presidente= 'Bakili Muluzi')]
list_Pais150 =  [Pais(    Code= 'MYS', Nombre =  'Malaysia', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '329758', AñoInde =  '1957', Poblacion =  '22244000', EsperanzaVida =   '70.8', NombreLocal = 'Malaysia', Gobierno =  'Constitutional Monarchy, Federation', Presidente= 'Salahuddin Abdul Aziz Shah Alhaj')]
list_Pais151 =  [Pais(    Code= 'MYT', Nombre =  'Mayotte', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '373', AñoInde =  '0', Poblacion =  '149000', EsperanzaVida =   '59.5', NombreLocal = 'Mayotte', Gobierno =  'Territorial Collectivity of France', Presidente= 'Jacques Chirac')]
list_Pais152 =  [Pais(    Code= 'NAM', Nombre =  'Namibia', Continente= 'Africa', Region = 'Southern Africa', Superficie= '824292', AñoInde =  '1990', Poblacion =  '1726000', EsperanzaVida =   '42.5', NombreLocal = 'Namibia', Gobierno =  'Republic', Presidente= 'Sam Nujoma')]
list_Pais153 =  [Pais(    Code= 'NCL',Nombre =  'New Caledonia', Continente= 'Oceania', Region = 'Melanesia', Superficie= '18575', AñoInde =  '0', Poblacion =  '214000', EsperanzaVida =   '72.8', NombreLocal = 'Nouvelle-Caledonie', Gobierno =  'Nonmetropolitan Territory of France', Presidente= 'Jacques Chirac')]
list_Pais154 =  [Pais(    Code= 'NER', Nombre =  'Niger', Continente= 'Africa', Region = 'Western Africa', Superficie= '1267000', AñoInde =  '1960', Poblacion =  '10730000', EsperanzaVida =   '41.3', NombreLocal = 'Niger', Gobierno =  'Republic', Presidente= 'Mamadou Tandja')]
list_Pais155 =  [Pais(    Code= 'NFK',Nombre =  'Norfolk Island', Continente= 'Oceania', Region = 'Australia and New Zealand', Superficie= '36', AñoInde =  '0',  Poblacion =  '2000', EsperanzaVida =   '0', NombreLocal = 'Norfolk Island', Gobierno =  'Territory of Australia', Presidente= 'Elisabeth II')]
list_Pais156 =  [Pais(    Code= 'NGA', Nombre =  'Nigeria', Continente= 'Africa', Region = 'Western Africa', Superficie= '923768', AñoInde =  '1960', Poblacion =  '111506000', EsperanzaVida =   '51.6', NombreLocal = 'Nigeria', Gobierno =  'Federal Republic', Presidente= 'Olusegun Obasanjo')]
list_Pais157 =  [Pais(    Code= 'NIC', Nombre =  'Nicaragua', Continente= 'North America', Region = 'Central America', Superficie= '130000', AñoInde =  '1838', Poblacion =  '5074000', EsperanzaVida =   '68.7', NombreLocal = 'Nicaragua', Gobierno =  'Republic', Presidente= 'Arnoldo Aleman Lacayo')]
list_Pais158 =  [Pais(    Code= 'NIU', Nombre =  'Niue', Continente= 'Oceania', Region = 'Polynesia', Superficie= '260', AñoInde =  '0', Poblacion =  '2000', EsperanzaVida =   '0', NombreLocal = 'Niue', Gobierno =  'Nonmetropolitan Territory of New Zealand', Presidente= 'Elisabeth II')]
list_Pais159 =  [Pais(    Code= 'NLD', Nombre =  'Netherlands', Continente= 'Europe', Region = 'Western Europe', Superficie= '41526', AñoInde =  '1581', Poblacion =  '15864000', EsperanzaVida =   '78.3', NombreLocal = 'Nederland', Gobierno =  'Constitutional Monarchy', Presidente= 'Willem-Alexander')]
list_Pais160 =  [Pais(    Code= 'NOR', Nombre =  'Norway', Continente= 'Europe', Region = 'Nordic Countries', Superficie= '323877', AñoInde =  '1905', Poblacion =  '4478500', EsperanzaVida =   '78.7', NombreLocal = 'Norge', Gobierno =  'Constitutional Monarchy',  Presidente= 'Harald V')]
list_Pais161 =  [Pais(    Code= 'NPL', Nombre =  'Nepal', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '147181', AñoInde =  '1769', Poblacion =  '23930000', EsperanzaVida =   '57.8', NombreLocal = 'Nepal', Gobierno =  'Constitutional Monarchy', Presidente= 'Gyanendra Bir Bikram')]
list_Pais162 =  [Pais(    Code= 'NRU', Nombre =  'Nauru', Continente= 'Oceania', Region = 'Micronesia', Superficie= '21', AñoInde =  '1968', Poblacion =  '12000', EsperanzaVida =   '60.8', NombreLocal = 'Naoero\/Nauru', Gobierno =  'Republic', Presidente= 'Bernard Dowiyogo')]
list_Pais163 =  [Pais(    Code= 'NZL', Nombre =  'New Zealand', Continente= 'Oceania', Region = 'Australia and New Zealand', Superficie= '270534',  AñoInde =  '1907', Poblacion =  '3862000', EsperanzaVida =   '77.8', NombreLocal = 'New Zealand\/Aotearoa', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais164 =  [Pais(    Code= 'OMN', Nombre =  'Oman', Continente= 'Asia', Region = 'Middle East', Superficie= '309500', AñoInde =  '1951', Poblacion =  '2542000', EsperanzaVida =   '71.8', NombreLocal = ' uman', Gobierno =  'Monarchy (Sultanate)', Presidente= 'Qabus ibn Sa id')]
list_Pais165 =  [Pais(    Code= 'PAK', Nombre =  'Pakistan', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '796095', AñoInde =  '1947', Poblacion =  '156483000', EsperanzaVida =   '61.1',NombreLocal = 'Pakistan', Gobierno =  'Republic', Presidente= 'Mohammad Rafiq Tarar')]
list_Pais166 =  [Pais(    Code= 'PAN', Nombre =  'Panama', Continente= 'North America', Region = 'Central America', Superficie= '75517', AñoInde =  '1903', Poblacion =  '2856000', EsperanzaVida =   '75.5', NombreLocal = 'Panama', Gobierno =  'Republic', Presidente= 'Mireya Elisa Moscoso RodrIguez')]
list_Pais167 =  [Pais(    Code= 'PCN', Nombre =  'Pitcairn', Continente= 'Oceania', Region = 'Polynesia', Superficie= '49', AñoInde =  '0', Poblacion =  '50', EsperanzaVida =   '0', NombreLocal = 'Pitcairn', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais168 =  [Pais(    Code= 'PER', Nombre =  'Peru', Continente= 'South America', Region = 'South America', Superficie= '1285216', AñoInde =  '1821', Poblacion =  '25662000', EsperanzaVida =   '70', NombreLocal = 'Peru\/Piruw', Gobierno =  'Republic',   Presidente= 'Valentin Paniagua Corazao')]
list_Pais169 =  [Pais(    Code= 'PHL',  Nombre =  'Philippines', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '300000', AñoInde =  '1946', Poblacion =  '75967000', EsperanzaVida =   '67.5', NombreLocal = 'Pilipinas', Gobierno =  'Republic', Presidente= 'Gloria Macapagal-Arroyo')]
list_Pais170 =  [Pais(    Code= 'PLW', Nombre =  'Palau', Continente= 'Oceania', Region = 'Micronesia', Superficie= '459', AñoInde =  '1994', Poblacion =  '19000', EsperanzaVida =   '68.6', NombreLocal = 'Belau\/Palau', Gobierno =  'Republic', Presidente= 'Kuniwo Nakamura')]
list_Pais171 =  [Pais(    Code= 'PNG', Nombre =  'Papua New Guinea', Continente= 'Oceania', Region = 'Melanesia', Superficie= '462840', AñoInde =  '1975', Poblacion =  '4807000', EsperanzaVida =   '63.1', NombreLocal = 'Papua New Guinea\/Papua Niugini', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais172 =  [Pais(    Code= 'POL', Nombre =  'Poland', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '323250', AñoInde =  '1918', Poblacion =  '38653600', EsperanzaVida =   '73.2', NombreLocal = 'Polska', Gobierno =  'Republic', Presidente= 'Aleksander Kwasniewski')]
list_Pais173 =  [Pais(    Code= 'PRI', Nombre =  'Puerto Rico', Continente= 'North America', Region = 'Caribbean', Superficie= '8875', AñoInde =  '0', Poblacion =  '3869000', EsperanzaVida =   '75.6', NombreLocal = 'Puerto Rico', Gobierno =  'Commonwealth of the uS', Presidente= 'George W. Bush')]
list_Pais174 =  [Pais(    Code= 'PRK', Nombre =  'North Korea', Continente= 'Asia', Region = 'Eastern Asia', Superficie= '120538', AñoInde =  '1948', Poblacion =  '24039000', EsperanzaVida =   '70.7', NombreLocal = 'Choson Minjujuui In min Konghwaguk (Bukhan)', Gobierno =  'Socialistic Republic', Presidente= 'Kim Jong-il')]
list_Pais175 =  [Pais(    Code= 'PRT', Nombre =  'Portugal', Continente= 'Europe', Region = 'Southern Europe', Superficie= '91982', AñoInde =  '1143', Poblacion =  '9997600', EsperanzaVida =   '75.8', NombreLocal = 'Portugal', Gobierno =  'Republic', Presidente= 'Jorge Sampaio')]
list_Pais176 =  [Pais(    Code= 'PRY', Nombre =  'Paraguay', Continente= 'South America', Region = 'South America', Superficie= '406752', AñoInde =  '1811', Poblacion =  '5496000', EsperanzaVida =   '73.7', NombreLocal = 'Paraguay', Gobierno =  'Republic', Presidente= 'Luis angel Gonzalez Macchi')]
list_Pais177 =  [Pais(    Code= 'PSE', Nombre =  'Palestine', Continente= 'Asia', Region = 'Middle East', Superficie= '6257', AñoInde =  '0', Poblacion =  '3101000', EsperanzaVida =   '71.4', NombreLocal = 'Filastin', Gobierno =  'Autonomous Area', Presidente= 'Yasser (Yasir) Arafat')]
list_Pais178 =  [Pais(    Code= 'PYF', Nombre =  'French Polynesia', Continente= 'Oceania', Region = 'Polynesia', Superficie= '4000', AñoInde =  '0', Poblacion =  '235000', EsperanzaVida =   '74.8', NombreLocal = 'Polynesie francaise', Gobierno =  'Nonmetropolitan Territory of France', Presidente= 'Jacques Chirac')]
list_Pais179 =  [Pais(    Code= 'QAT', Nombre =  'Qatar', Continente= 'Asia', Region = 'Middle East', Superficie= '11000', AñoInde =  '1971', Poblacion =  '599000', EsperanzaVida =   '72.4', NombreLocal = 'Qatar', Gobierno =  'Monarchy', Presidente= 'Hamad ibn Khalifa al-Thani')]
list_Pais180 =  [Pais(    Code= 'REU', Nombre =  'Reunion', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '2510', AñoInde =  '0', Poblacion =  '699000', EsperanzaVida =   '72.7', NombreLocal = 'Reunion', Gobierno =  'Overseas Department of France', Presidente= 'Jacques Chirac')]
list_Pais181 =  [Pais(    Code= 'ROM', Nombre =  'Romania', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '238391', AñoInde =  '1878', Poblacion =  '22455500', EsperanzaVida =   '69.9', NombreLocal = 'Romania', Gobierno =  'Republic', Presidente= 'Ion Iliescu')]
list_Pais182 =  [Pais(    Code= 'RUS', Nombre =  'Russian Federation', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '17075400', AñoInde =  '1991', Poblacion =  '146934000', EsperanzaVida =   '67.2', NombreLocal = 'Rossija', Gobierno =  'Federal Republic', Presidente= 'Vladimir Putin')]
list_Pais183 =  [Pais(    Code= 'RWA', Nombre =  'Rwanda', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '26338', AñoInde =  '1962', Poblacion =  '7733000', EsperanzaVida =   '39.3', NombreLocal = 'Rwanda\/urwanda', Gobierno =  'Republic', Presidente= 'Paul Kagame')]
list_Pais184 =  [Pais(    Code= 'SAU', Nombre =  'Saudi Arabia', Continente= 'Asia', Region = 'Middle East', Superficie= '2149690', AñoInde =  '1932', Poblacion =  '21607000', EsperanzaVida =   '67.8', NombreLocal = 'Al- Arabiya as-Sa udiya', Gobierno =  'Monarchy', Presidente= 'Fahd ibn Abdul-Aziz al-Sa ud')]
list_Pais185 =  [Pais(    Code= 'SDN', Nombre =  'Sudan', Continente= 'Africa', Region = 'Northern Africa', Superficie= '2505813', AñoInde =  '1956', Poblacion =  '29490000', EsperanzaVida =   '56.6', NombreLocal = 'As-Sudan', Gobierno =  'Islamic Republic', Presidente= 'Omar Hassan Ahmad al-Bashir')]
list_Pais186 =  [Pais(    Code= 'SEN', Nombre =  'Senegal', Continente= 'Africa', Region = 'Western Africa', Superficie= '196722', AñoInde =  '1960', Poblacion =  '9481000', EsperanzaVida =   '62.2', NombreLocal = 'Senegal\/Sounougal', Gobierno =  'Republic', Presidente= 'Abdoulaye Wade')]
list_Pais187 =  [Pais(    Code= 'SGP', Nombre =  'Singapore', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '618', AñoInde =  '1965', Poblacion =  '3567000', EsperanzaVida =   '80.1', NombreLocal = 'Singapore\/Singapura\/Xinjiapo\/Singapur', Gobierno =  'Republic', Presidente= 'Sellapan Rama Nathan')]
list_Pais188 =  [Pais(    Code= 'SGS', Nombre =  'South Georgia and the South Sandwich Islands', Continente= 'Antarctica', Region = 'Antarctica', Superficie= '3903', AñoInde =  '0', Poblacion =  '0', EsperanzaVida =   '0', NombreLocal = 'South Georgia and the South Sandwich Islands', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais189 =  [Pais(    Code= 'SHN',   Nombre =  'Saint Helena', Continente= 'Africa', Region = 'Western Africa',    Superficie= '314',  AñoInde =  '0',    Poblacion =  '6000',    EsperanzaVida =   '76.8',   NombreLocal = 'Saint Helena', Gobierno =  'Dependent Territory of the uK',  Presidente= 'Elisabeth II')]
list_Pais190 =  [Pais(    Code= 'SJM', Nombre =  'Svalbard and Jan Mayen', Continente= 'Europe', Region = 'Nordic Countries', Superficie= '62422', AñoInde =  '0', Poblacion =  '3200', EsperanzaVida =   '0', NombreLocal = 'Svalbard og Jan Mayen', Gobierno =  'Dependent Territory of Norway', Presidente= 'Harald V')]
list_Pais191 =  [Pais(    Code= 'SLB', Nombre =  'Solomon Islands', Continente= 'Oceania', Region = 'Melanesia', Superficie= '28896', AñoInde =  '1978', Poblacion =  '444000', EsperanzaVida =   '71.3', NombreLocal = 'Solomon Islands', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais192 =  [Pais(    Code= 'SLE', Nombre =  'Sierra Leone', Continente= 'Africa', Region = 'Western Africa', Superficie= '71740', AñoInde =  '1961', Poblacion =  '4854000', EsperanzaVida =   '45.3',  NombreLocal = 'Sierra Leone', Gobierno =  'Republic', Presidente= 'Ahmed Tejan Kabbah')]
list_Pais193 =  [Pais(    Code= 'SLV', Nombre =  'El Salvador', Continente= 'North America', Region = 'Central America', Superficie= '21041', AñoInde =  '1841', Poblacion =  '6276000', EsperanzaVida =   '69.7', NombreLocal = 'El Salvador', Gobierno =  'Republic', Presidente= 'Francisco Guillermo Flores Perez')]
list_Pais194 =  [Pais(    Code= 'SMR', Nombre =  'San Marino', Continente= 'Europe', Region = 'Southern Europe', Superficie= '61', AñoInde =  '885', Poblacion =  '27000', EsperanzaVida =   '81.1', NombreLocal = 'San Marino', Gobierno =  'Republic', Presidente= 'NuLL')]
list_Pais195 =  [Pais(    Code= 'SOM', Nombre =  'Somalia', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '637657', AñoInde =  '1960', Poblacion =  '10097000', EsperanzaVida =   '46.2', NombreLocal = 'Soomaaliya', Gobierno =  'Republic', Presidente= 'Abdiqassim Salad Hassan')]
list_Pais196 =  [Pais(    Code= 'SPM', Nombre =  'Saint Pierre and Miquelon', Continente= 'North America', Region = 'North America', Superficie= '242', AñoInde =  '0', Poblacion =  '7000', EsperanzaVida =   '77.6', NombreLocal = 'Saint-Pierre-et-Miquelon', Gobierno =  'Territorial Collectivity of France', Presidente= 'Jacques Chirac')]
list_Pais197 =  [Pais(    Code= 'STP', Nombre =  'Sao Tome and Principe', Continente= 'Africa', Region = 'Central Africa', Superficie= '964', AñoInde =  '1975', Poblacion =  '147000', EsperanzaVida =   '65.3', NombreLocal = 'Sao Tome e PrIncipe', Gobierno =  'Republic',   Presidente= 'Miguel Trovoada')]
list_Pais198 =  [Pais(    Code= 'SUR', Nombre =  'Suriname', Continente= 'South America', Region = 'South America', Superficie= '163265', AñoInde =  '1975', Poblacion =  '417000', EsperanzaVida =   '71.4', NombreLocal = 'Suriname', Gobierno =  'Republic', Presidente= 'Ronald Venetiaan')]
list_Pais199 =  [Pais(    Code= 'SVK', Nombre =  'Slovakia', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '49012', AñoInde =  '1993', Poblacion =  '5398700', EsperanzaVida =   '73.7',NombreLocal = 'Slovensko', Gobierno =  'Republic', Presidente= 'Rudolf Schuster')]
list_Pais200 =  [Pais(    Code= 'SVN', Nombre =  'Slovenia', Continente= 'Europe', Region = 'Southern Europe', Superficie= '20256', AñoInde =  '1991', Poblacion =  '1987800', EsperanzaVida =   '74.9',   NombreLocal = 'Slovenija', Gobierno =  'Republic', Presidente= 'Milan Kucan')]
list_Pais201 =  [Pais(    Code= 'SWE', Nombre =  'Sweden', Continente= 'Europe', Region = 'Nordic Countries', Superficie= '449964', AñoInde =  '836', Poblacion =  '8861400', EsperanzaVida =   '79.6', NombreLocal = 'Sverige', Gobierno =  'Constitutional Monarchy', Presidente= 'Carl XVI Gustaf')]
list_Pais202 =  [Pais(    Code= 'SWZ', Nombre =  'Swaziland', Continente= 'Africa', Region = 'Southern Africa', Superficie= '17364', AñoInde =  '1968', Poblacion =  '1008000', EsperanzaVida =   '40.4', NombreLocal = 'kaNgwane', Gobierno =  'Monarchy', Presidente= 'Mswati III')]
list_Pais203 =  [Pais(    Code= 'SYC', Nombre =  'Seychelles', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '455', AñoInde =  '1976', Poblacion =  '77000', EsperanzaVida =   '70.4', NombreLocal = 'Sesel\/Seychelles', Gobierno =  'Republic', Presidente= 'France-Albert Rene')]
list_Pais204 =  [Pais(    Code= 'SYR', Nombre =  'Syria', Continente= 'Asia', Region = 'Middle East', Superficie= '185180', AñoInde =  '1941', Poblacion =  '16125000', EsperanzaVida =   '68.5', NombreLocal = 'Suriya', Gobierno =  'Republic', Presidente= 'Bashar al-Assad')]
list_Pais205 =  [Pais(    Code= 'TCA', Nombre =  'Turks and Caicos Islands', Continente= 'North America', Region = 'Caribbean', Superficie= '430', AñoInde =  '0', Poblacion =  '17000', EsperanzaVida =   '73.3', NombreLocal = 'The Turks and Caicos Islands', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais206 =  [Pais(    Code= 'TCD', Nombre =  'Chad', Continente= 'Africa', Region = 'Central Africa', Superficie= '1284000', AñoInde =  '1960', Poblacion =  '7651000', EsperanzaVida =   '50.5', NombreLocal = 'Tchad\/Tshad', Gobierno =  'Republic', Presidente= 'Idriss Deby')]
list_Pais207 =  [Pais(    Code= 'TGO', Nombre =  'Togo', Continente= 'Africa', Region = 'Western Africa', Superficie= '56785', AñoInde =  '1960', Poblacion =  '4629000', EsperanzaVida =   '54.7', NombreLocal = 'Togo', Gobierno =  'Republic', Presidente= 'Gnassingbe Eyadema')]
list_Pais208 =  [Pais(    Code= 'THA', Nombre =  'Thailand', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '513115', AñoInde =  '1350', Poblacion =  '61399000', EsperanzaVida =   '68.6', NombreLocal = 'Prathet Thai', Gobierno =  'Constitutional Monarchy', Presidente= 'Bhumibol Adulyadej')]
list_Pais209 =  [Pais(    Code= 'TJK', Nombre =  'Tajikistan', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '143100', AñoInde =  '1991', Poblacion =  '6188000', EsperanzaVida =   '64.1', NombreLocal = 'Tocikiston', Gobierno =  'Republic', Presidente= 'Emomali Rahmonov')]
list_Pais210 =  [Pais(    Code= 'TKL',Nombre =  'Tokelau', Continente= 'Oceania', Region = 'Polynesia', Superficie= '12', AñoInde =  '0', Poblacion =  '2000', EsperanzaVida =   '0', NombreLocal = 'Tokelau', Gobierno =  'Nonmetropolitan Territory of New Zealand', Presidente= 'Elisabeth II')]
list_Pais211 =  [Pais(    Code= 'TKM', Nombre =  'Turkmenistan', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '488100', AñoInde =  '1991', Poblacion =  '4459000', EsperanzaVida =   '60.9', NombreLocal = 'Turkmenostan', Gobierno =  'Republic', Presidente= 'Saparmurad Nijazov')]
list_Pais212 =  [Pais(    Code= 'TMP', Nombre =  'East Timor', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '14874', AñoInde =  '0', Poblacion =  '885000', EsperanzaVida =   '46', NombreLocal = 'Timor Timur', Gobierno =  'Administrated by the uN', Presidente= 'Jose Alexandre Gusmao'),
]
list_Pais213 =  [Pais(    Code= 'TON', Nombre =  'Tonga', Continente= 'Oceania', Region = 'Polynesia', Superficie= '650', AñoInde =  '1970', Poblacion =  '99000', EsperanzaVida =   '67.9',  NombreLocal = 'Tonga', Gobierno =  'Monarchy', Presidente= 'Taufa ahau Tupou IV')]
list_Pais214 =  [Pais(    Code= 'TTO', Nombre =  'Trinidad and Tobago', Continente= 'North America', Region = 'Caribbean', Superficie= '5130', AñoInde =  '1962', Poblacion =  '1295000', EsperanzaVida =   '68', NombreLocal = 'Trinidad and Tobago', Gobierno =  'Republic', Presidente= 'Arthur N. R. Robinson')]
list_Pais215 =  [Pais(    Code= 'TUN', Nombre =  'Tunisia', Continente= 'Africa', Region = 'Northern Africa', Superficie= '163610', AñoInde =  '1956', Poblacion =  '9586000', EsperanzaVida =   '73.7', NombreLocal = 'Tunis\/Tunisie', Gobierno =  'Republic', Presidente= 'Zine al-Abidine Ben Ali')]
list_Pais216 =  [Pais(    Code= 'TUR', Nombre =  'Turkey', Continente= 'Asia', Region = 'Middle East', Superficie= '774815', AñoInde =  '1923', Poblacion =  '66591000', EsperanzaVida =   '71', NombreLocal = 'Turkiye', Gobierno =  'Republic', Presidente= 'Ahmet Necdet Sezer')]
list_Pais217 =  [Pais(    Code= 'TUV',Nombre =  'Tuvalu',Continente= 'Oceania', Region = 'Polynesia',Superficie= '26', AñoInde =  '1978', Poblacion =  '12000', EsperanzaVida =   '66.3', NombreLocal = 'Tuvalu', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais218 =  [Pais(    Code= 'TWN', Nombre =  'Taiwan',Continente= 'Asia', Region = 'Eastern Asia', Superficie= '36188', AñoInde =  '1945', Poblacion =  '22256000', EsperanzaVida =   '76.4', NombreLocal = 'Tai-wan', Gobierno =  'Republic', Presidente= 'Chen Shui-bian')]
list_Pais219 =  [Pais(    Code= 'TZA', Nombre =  'Tanzania', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '883749', AñoInde =  '1961', Poblacion =  '33517000', EsperanzaVida =   '52.3', NombreLocal = 'Tanzania', Gobierno =  'Republic', Presidente= 'Benjamin William Mkapa')]
list_Pais220 =  [Pais(    Code= 'UGA', Nombre =  'uganda', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '241038', AñoInde =  '1962', Poblacion =  '21778000', EsperanzaVida =   '42.9', NombreLocal = 'uganda', Gobierno =  'Republic', Presidente= 'Yoweri Museveni')]
list_Pais221 =  [Pais(    Code= 'UKR', Nombre =  'ukraine', Continente= 'Europe', Region = 'Eastern Europe', Superficie= '603700', AñoInde =  '1991', Poblacion =  '50456000', EsperanzaVida =   '66', NombreLocal = 'ukrajina', Gobierno =  'Republic', Presidente= 'Leonid KutSma')]
list_Pais222 =  [Pais(    Code= 'UMI', Nombre =  'united States Minor Outlying Islands', Continente= 'Oceania', Region = 'Micronesia\/Caribbean', Superficie= '16', AñoInde =  '0', Poblacion =  '0', EsperanzaVida =   '0', NombreLocal = 'united States Minor Outlying Islands', Gobierno =  'Dependent Territory of the uS', Presidente= 'George W. Bush')]
list_Pais223 =  [Pais(    Code= 'URY', Nombre =  'uruguay', Continente= 'South America', Region = 'South America', Superficie= '175016', AñoInde =  '1828', Poblacion =  '3337000', EsperanzaVida =   '75.2', NombreLocal = 'uruguay', Gobierno =  'Republic', Presidente= 'Jorge Batlle Ibanez')]
list_Pais224 =  [Pais(    Code= 'USA', Nombre =  'united States', Continente= 'North America', Region = 'North America', Superficie= '9363520', AñoInde =  '1776', Poblacion =  '278357000', EsperanzaVida =   '77.1', NombreLocal = 'united States', Gobierno =  'Federal Republic', Presidente= 'George W. Bush')]
list_Pais225 =  [Pais(    Code= 'UZB', Nombre =  'uzbekistan', Continente= 'Asia', Region = 'Southern and Central Asia', Superficie= '447400', AñoInde =  '1991', Poblacion =  '24318000', EsperanzaVida =   '63.7', NombreLocal = 'uzbekiston', Gobierno =  'Republic', Presidente= 'Islam Karimov')]
list_Pais226 =  [Pais(    Code= 'VAT', Nombre =  'Holy See (Vatican City State)', Continente= 'Europe', Region = 'Southern Europe', Superficie= '0', AñoInde =  '1929', Poblacion =  '1000', EsperanzaVida =   '0', NombreLocal = 'Santa Sede\/Citta del Vaticano', Gobierno = 'Independent Church State', Presidente = 'Johannes Paavali II')]
list_Pais227 =  [Pais(    Code= 'VCT', Nombre =  'Saint Vincent and the Grenadines', Continente= 'North America', Region = 'Caribbean', Superficie= '388', AñoInde =  '1979', Poblacion =  '114000', EsperanzaVida =   '72.3', NombreLocal = 'Saint Vincent and the Grenadines', Gobierno =  'Constitutional Monarchy', Presidente= 'Elisabeth II')]
list_Pais228 =  [Pais(    Code= 'VEN', Nombre =  'Venezuela', Continente= 'South America', Region = 'South America', Superficie= '912050', AñoInde =  '1811', Poblacion =  '24170000', EsperanzaVida =   '73.1', NombreLocal = 'Venezuela', Gobierno =  'Federal Republic', Presidente= 'Hugo Chavez FrIas')]
list_Pais229 =  [Pais(    Code= 'VGB', Nombre =  'Virgin Islands, British', Continente= 'North America', Region = 'Caribbean', Superficie= '151', AñoInde =  '0', Poblacion =  '21000', EsperanzaVida =   '75.4', NombreLocal = 'British Virgin Islands', Gobierno =  'Dependent Territory of the uK', Presidente= 'Elisabeth II')]
list_Pais230 =  [Pais(    Code= 'VIR', Nombre =  'Virgin Islands, u.S.', Continente= 'North America', Region = 'Caribbean', Superficie= '347', AñoInde =  '0', Poblacion =  '93000', EsperanzaVida =   '78.1', NombreLocal = 'Virgin Islands of the united States', Gobierno =  'uS Territory', Presidente= 'George W. Bush')]
list_Pais231 =  [Pais(    Code= 'VNM', Nombre =  'Vietnam', Continente= 'Asia', Region = 'Southeast Asia', Superficie= '331689', AñoInde =  '1945', Poblacion =  '79832000', EsperanzaVida =   '69.3', NombreLocal = 'Viet Nam', Gobierno =  'Socialistic Republic', Presidente= 'Tran Duc Luong')]
list_Pais232 =  [Pais(    Code= 'VUT', Nombre =  'Vanuatu', Continente= 'Oceania', Region = 'Melanesia', Superficie= '12189', AñoInde =  '1980', Poblacion =  '190000' , EsperanzaVida =   '60.6', NombreLocal = 'Vanuatu', Gobierno =  'Republic', Presidente= 'John Bani')]
list_Pais233 =  [Pais(    Code= 'WLF', Nombre =  'Wallis and Futuna', Continente= 'Oceania', Region = 'Polynesia', Superficie= '200', AñoInde =  '0', Poblacion =  '15000', EsperanzaVida =   '0', NombreLocal = 'Wallis-et-Futuna', Gobierno =  'Nonmetropolitan Territory of France', Presidente= 'Jacques Chirac')]
list_Pais234 =  [Pais(    Code= 'WSM', Nombre =  'Samoa', Continente= 'Oceania', Region = 'Polynesia', Superficie= '2831', AñoInde =  '1962', Poblacion = '180000',  EsperanzaVida =   '69.2', NombreLocal = 'Samoa', Gobierno =  'Parlementary Monarchy', Presidente= 'Malietoa Tanumafili II')]
list_Pais235 =  [Pais(    Code= 'YEM', Nombre =  'Yemen', Continente= 'Asia', Region = 'Middle East', Superficie= '527968', AñoInde =  '1918', Poblacion =  '18112000', EsperanzaVida =   '59.8', NombreLocal = 'Al-Yaman', Gobierno =  'Republic', Presidente= 'Ali Abdallah Salih')]
list_Pais236 =  [Pais(    Code= 'YUG', Nombre =  'Yugoslavia',Continente= 'Europe', Region = 'Southern Europe', Superficie= '102173', AñoInde =  '1918', Poblacion =  '10640000', EsperanzaVida =   '72.4', NombreLocal = 'Jugoslavija', Gobierno =  'Federal Republic', Presidente= 'Vojislav KoStunica')]
list_Pais237 =  [Pais(    Code= 'ZAF', Nombre =  'South Africa', Continente= 'Africa', Region = 'Southern Africa', Superficie= '1221037', AñoInde =  '1910', Poblacion =  '40377000', EsperanzaVida =   '51.1', NombreLocal = 'South Africa', Gobierno =  'Republic', Presidente= 'Thabo Mbeki')]
list_Pais238 =  [Pais(    Code= 'ZMB',Nombre =  'Zambia', Continente= 'Africa', Region = 'Eastern Africa', Superficie= '752618', AñoInde =  '1964', Poblacion = '9169000', EsperanzaVida =   '37.2', NombreLocal = 'Zambia', Gobierno =  'Republic', Presidente= 'Frederick Chiluba')]
list_Pais239 =  [Pais(    Code= 'ZWE',Nombre =  'Zimbabwe',Continente= 'Africa',Region = 'Eastern Africa',Superficie= '390757',AñoInde =  '1980',Poblacion =  '11669000',EsperanzaVida =   '37.8',NombreLocal = 'Zimbabwe',Gobierno =  'Republic',Presidente= 'Robert G. Mugabe')]

######################################################################### GET ###############################################################################################
@app.get("/ExamenParcial/continente/region/{Code}", status_code=200)
async def get_Pais(Code:str):
    if Code == 'ABW':
        return list_Pais1
    elif Code == 'AFG':
        return list_Pais2
    elif Code == 'AGO':
        return list_Pais3
    elif Code == 'AIA':
        return list_Pais4
    elif Code == 'ALB':
        return list_Pais5
    elif Code == 'AND':
        return list_Pais6
    elif Code == 'ANT':
        return list_Pais7
    elif Code == 'ARE':
        return list_Pais8
    elif Code == 'ARG':
        return list_Pais9
    elif Code == 'ARM':
        return list_Pais10
    elif Code == 'ASM':
        return list_Pais11
    elif Code == 'ATA':
        return list_Pais12
    elif Code == 'ATF':
        return list_Pais13
    elif Code == 'ATG':
        return list_Pais14
    elif Code == 'AUS':
        return list_Pais15
    elif Code == 'AUT':
        return list_Pais16
    elif Code == 'AZE':
        return list_Pais17
    elif Code == 'BOI':
        return list_Pais18
    elif Code == 'BEL':
        return list_Pais19
    elif Code == 'BEN':
        return list_Pais20
    elif Code == 'BFA':
        return list_Pais21
    elif Code == 'BGD':
        return list_Pais22
    elif Code == 'BGR':
        return list_Pais23
    elif Code == 'BHR':
        return list_Pais24
    elif Code == 'BHS':
        return list_Pais25
    elif Code == 'BIH':
        return list_Pais26
    elif Code == 'BLR':
        return list_Pais27
    elif Code == 'BLZ':
        return list_Pais28
    elif Code == 'BMU':
        return list_Pais29
    elif Code == 'BOL':
        return list_Pais30
    elif Code == 'BRA':
        return list_Pais31
    elif Code == 'BRB':
        return list_Pais32
    elif Code == 'BRN':
        return list_Pais33
    elif Code == 'BTN':
        return list_Pais34
    elif Code == 'BVT':
        return list_Pais35
    elif Code == 'BWA':
        return list_Pais36
    elif Code == 'CAF':
        return list_Pais37
    elif Code == 'CAN':
        return list_Pais38
    elif Code == 'CCK':
        return list_Pais39
    elif Code == 'CHE':
        return list_Pais40
    elif Code == 'CHL':
        return list_Pais41
    elif Code == 'CHN':
        return list_Pais42
    elif Code == 'CIV':
        return list_Pais43
    elif Code == 'CMR':
        return list_Pais44
    elif Code == 'COD':
        return list_Pais45
    elif Code == 'COG':
        return list_Pais46
    elif Code == 'COK':
        return list_Pais47
    elif Code == 'COL':
        return list_Pais48
    elif Code == 'COM':
        return list_Pais49
    elif Code == 'CPV':
        return list_Pais50
    elif Code == 'CRI':
        return list_Pais51
    elif Code == 'CUB':
        return list_Pais52
    elif Code == 'CXR':
        return list_Pais53
    elif Code == 'CYP':
        return list_Pais54
    elif Code == 'CYM':
        return list_Pais55
    elif Code == 'CZE':
        return list_Pais56
    elif Code == 'DEU':
        return list_Pais57
    elif Code == 'DJI':
        return list_Pais58
    elif Code == 'DMA':
        return list_Pais59
    elif Code == 'DNK':
        return list_Pais60
    elif Code == 'DOM':
        return list_Pais61
    elif Code == 'DZA':
        return list_Pais62
    elif Code == 'ECU':
        return list_Pais63
    elif Code == 'EGY':
        return list_Pais64
    elif Code == 'ERI':
        return list_Pais65
    elif Code == 'ESH':
        return list_Pais66
    elif Code == 'ESP':
        return list_Pais67
    elif Code == 'EST':
        return list_Pais68
    elif Code == 'ETH':
        return list_Pais69
    elif Code == 'FIN':
        return list_Pais70
    elif Code == 'FJI':
        return list_Pais71
    elif Code == 'FLK':
        return list_Pais72
    elif Code == 'FRA':
        return list_Pais73
    elif Code == 'FRO':
        return list_Pais74
    elif Code == 'FSH':
        return list_Pais75
    elif Code == 'GAB':
        return list_Pais76
    elif Code == 'GBR':
        return list_Pais77
    elif Code == 'GEO':
        return list_Pais78
    elif Code == 'GHA':
        return list_Pais79
    elif Code == 'GIB':
        return list_Pais80
    elif Code == 'GIN':
        return list_Pais81
    elif Code == 'GLP':
        return list_Pais82
    elif Code == 'GMB':
        return list_Pais83
    elif Code == 'GNB':
        return list_Pais84
    elif Code == 'GNQ':
        return list_Pais85
    elif Code == 'GRC':
        return list_Pais86
    elif Code == 'GRD':
        return list_Pais87
    elif Code == 'GRL':
        return list_Pais88
    elif Code == 'GTM':
        return list_Pais89
    elif Code == 'GUF':
        return list_Pais90
    elif Code == 'GUM':
        return list_Pais91
    elif Code == 'GUY':
        return list_Pais92
    elif Code == 'HKG':
        return list_Pais93
    elif Code == 'HMD':
        return list_Pais94
    elif Code == 'HND':
        return list_Pais95
    elif Code == 'HRV':
        return list_Pais96
    elif Code == 'HTI':
        return list_Pais97
    elif Code == 'HUN':
        return list_Pais98
    elif Code == 'IDN':
        return list_Pais99
    elif Code == 'IND':
        return list_Pais100
    elif Code == 'IOT':
        return list_Pais101
    elif Code == 'IRL':
        return list_Pais102
    elif Code == 'IRN':
        return list_Pais103
    elif Code == 'IRQ':
        return list_Pais104
    elif Code == 'ISL':
        return list_Pais105
    elif Code == 'ISR':
        return list_Pais106
    elif Code == 'ITA':
        return list_Pais107
    elif Code == 'JAM':
        return list_Pais108
    elif Code == 'JOR':
        return list_Pais109
    elif Code == 'JPN':
        return list_Pais110
    elif Code == 'KAZ':
        return list_Pais111
    elif Code == 'KEN':
        return list_Pais112
    elif Code == 'KGZ':
        return list_Pais113
    elif Code == 'KHM':
        return list_Pais114
    elif Code == 'KIR':
        return list_Pais115
    elif Code == 'KNA':
        return list_Pais116
    elif Code == 'KOR':
        return list_Pais117
    elif Code == 'KWT':
        return list_Pais118
    elif Code == 'LAO':
        return list_Pais119
    elif Code == 'LBN':
        return list_Pais120
    elif Code == 'LBR':
        return list_Pais121
    elif Code == 'LBY':
        return list_Pais122
    elif Code == 'LCA':
        return list_Pais123
    elif Code == 'LIE':
        return list_Pais124
    elif Code == 'LKA':
        return list_Pais125
    elif Code == 'LSO':
        return list_Pais126
    elif Code == 'LTU':
        return list_Pais127
    elif Code == 'LUX':
        return list_Pais128
    elif Code == 'LVA':
        return list_Pais129
    elif Code == 'MAC':
        return list_Pais130
    elif Code == 'MAR':
        return list_Pais131
    elif Code == 'MCO':
        return list_Pais132
    elif Code == 'MDA':
        return list_Pais133
    elif Code == 'MDG':
        return list_Pais134
    elif Code == 'MDV':
        return list_Pais135
    elif Code == ' MEX':
        return list_Pais136
    elif Code == 'MHL':
        return list_Pais137
    elif Code == 'MKD':
        return list_Pais138
    elif Code == 'MLI':
        return list_Pais139
    elif Code == 'MLT':
        return list_Pais140
    elif Code == 'MMR':
        return list_Pais141
    elif Code == 'MNG':
        return list_Pais142
    elif Code == 'MNP':
        return list_Pais143
    elif Code == 'MOZ':
        return list_Pais144
    elif Code == 'MRT':
        return list_Pais145
    elif Code == 'MSR':
        return list_Pais146
    elif Code == 'MTQ':
        return list_Pais147
    elif Code == 'MUS':
        return list_Pais148
    elif Code == 'MWI':
        return list_Pais149
    elif Code == 'MYS':
        return list_Pais150
    elif Code == 'MYT':
        return list_Pais151
    elif Code == 'NAM':
        return list_Pais152
    elif Code == 'NCL':
        return list_Pais153
    elif Code == 'NER':
        return list_Pais154
    elif Code == 'NFK':
        return list_Pais155
    elif Code == 'NGA':
        return list_Pais156
    elif Code == 'NIC':
        return list_Pais157
    elif Code == 'NIU':
        return list_Pais158
    elif Code == 'NLD':
        return list_Pais159
    elif Code == 'NOR':
        return list_Pais160
    elif Code == 'NPL':
        return list_Pais161
    elif Code == 'NRU':
        return list_Pais162
    elif Code == 'NZL':
        return list_Pais163
    elif Code == 'OMN':
        return list_Pais164
    elif Code == 'PAK':
        return list_Pais165
    elif Code == 'PAN':
        return list_Pais166
    elif Code == 'PCN':
        return list_Pais167
    elif Code == 'PER':
        return list_Pais168
    elif Code == 'PHL':
        return list_Pais169
    elif Code == 'PLW':
        return list_Pais170
    elif Code == 'PNG':
        return list_Pais171
    elif Code == 'POL':
        return list_Pais172
    elif Code == 'PRI':
        return list_Pais173
    elif Code == 'PRK':
        return list_Pais174
    elif Code == 'PRT':
        return list_Pais175
    elif Code == 'PRY':
        return list_Pais176
    elif Code == 'PSE':
        return list_Pais177
    elif Code == 'PYF':
        return list_Pais178
    elif Code == 'QAT':
        return list_Pais179
    elif Code == 'REU':
        return list_Pais180
    elif Code == 'ROM':
        return list_Pais181
    elif Code == 'RUS':
        return list_Pais182
    elif Code == 'RWA':
        return list_Pais183
    elif Code == 'SAU':
        return list_Pais184
    elif Code == 'SDN':
        return list_Pais185
    elif Code == 'SEN':
        return list_Pais186
    elif Code == 'SGP':
        return list_Pais187
    elif Code == 'SGS':
        return list_Pais188
    elif Code == 'SHN':
        return list_Pais189
    elif Code == 'SJM':
        return list_Pais190
    elif Code == 'SLB':
        return list_Pais191
    elif Code == 'SLE':
        return list_Pais192
    elif Code == 'SLV':
        return list_Pais193
    elif Code == 'SMR':
        return list_Pais194
    elif Code == 'SOM':
        return list_Pais195
    elif Code == 'SPM':
        return list_Pais196
    elif Code == 'STP':
        return list_Pais197
    elif Code == 'SUR':
        return list_Pais198
    elif Code == 'SVK':
        return list_Pais199
    elif Code == 'SVN':
        return list_Pais200
    elif Code == 'SWE':
        return list_Pais201
    elif Code == 'SWZ':
        return list_Pais202
    elif Code == 'SYC':
        return list_Pais203
    elif Code == 'SYR':
        return list_Pais204
    elif Code == 'TCA':
        return list_Pais205
    elif Code == 'TCD':
        return list_Pais206
    elif Code == 'TGO':
        return list_Pais207
    elif Code == 'THA':
        return list_Pais208
    elif Code == 'TJK':
        return list_Pais209
    elif Code == 'TKL':
        return list_Pais210
    elif Code == 'TKM':
        return list_Pais211
    elif Code == 'TMP':
        return list_Pais212
    elif Code =='TON':
        return list_Pais213
    elif Code == 'TTO':
        return list_Pais214
    elif Code == 'TUN':
        return list_Pais215
    elif Code == 'TUR':
        return list_Pais216
    elif Code == 'TUV':
        return list_Pais217
    elif Code == 'TWN':
        return list_Pais218
    elif Code == 'TZA':
        return list_Pais219
    elif Code == 'UGA':
        return list_Pais220
    elif Code == 'UKR':
        return list_Pais221
    elif Code == 'UMI':
        return list_Pais222
    elif Code == 'URY':
        return list_Pais223
    elif Code == 'USA':
        return list_Pais224
    elif Code == 'UZB':
        return list_Pais225
    elif Code == 'VAT':
        return list_Pais226
    elif Code == 'VCT':
        return list_Pais227
    elif Code == 'VEN':
        return list_Pais228
    elif Code == 'VGB':
        return list_Pais229
    elif Code == 'VIR':
        return list_Pais230
    elif Code == 'VNM':
        return list_Pais231
    elif Code == 'VUT':
        return list_Pais232
    elif Code == 'WLF':
        return list_Pais233
    elif Code == 'WSM':
        return list_Pais234
    elif Code =='YEM ':
        return list_Pais235
    elif Code == 'YUG':
        return list_Pais236
    elif Code =='ZAF':
        return list_Pais237
    elif Code == 'ZMB':
        return list_Pais238
    elif Code == 'ZWE':
        return list_Pais239
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL Incorrecta, intentelo de nuevo")


######################################################################### GET ###############################################################################################
@app.get("/ExamenParcial/{main}",status_code=status.HTTP_200_OK)
async def main(main:str):
    if main == 'main':
        return {"message":"Bienvenido al Examen Parcial"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL Incorrecta, intentelo de nuevo")
