import logging
import os
import datetime
import requests
import configdf
import pandas as pd
import models
from bs4 import BeautifulSoup

logging.basicConfig(
    filename='main.log',
    level='DEBUG',
    format="%(asctime)s:%(levelname)s:%(message)s"
)

logging.debug('Inicio del programa.')

"""Diccionario con los links que van a pasar a nuestra funcion"""
links_to_transform = {
    'bibliotecas' : 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7',
    'cines' : 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
    'museos' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/archivo/4207def0-2ff7-41d5-9095-d42ae8207a5d',
}

"""codificamos la fecha para poder usarlas en la creacion de carpetas y archivos"""
today = datetime.date.today().strftime('-%d-%m-%Y')
year_month = datetime.date.today().strftime('%Y-%m') 

"""Funcion que toma el diccionario, toma los 2 items y los transforma en variables.
luego llama a la url con requests y la acomoda con BeautifulSoup, filtramos las etiquetas hasta encontrar nuestros links de descarga.
Hacemos uso de reques para descargar el link del archivo csv, definimos la ruta codificada con nombre y fecha, creamos el directorio, y los archivos correspondientes.
"""
try:
    dirs_dict = {}
    for k,v in links_to_transform.items():
        name = k
        url = v
        page = requests.get(url) #llamamos la pagina web
        
        soup = BeautifulSoup(page.content, 'html.parser') #acomodamos el request en el formato html
        get_links = soup.find("a", "btn btn-green btn-block") #filtramos la clase y etiqueta
        links = get_links.attrs.get('href') #filtramos el contenedor del link
        link_to_dowload = requests.get(links, stream = True) #leemos el link que contiene la descarga
        c_subc = os.path.join("datos",name,year_month) #creamos la ruta con nombre y fecha
        dirs_dict[k]=str(c_subc+f'\\{name}{today}.csv') #guardarmos los path para conectarnos
        os.makedirs(c_subc, exist_ok=True) #creamos el directorio
        with open(c_subc+f'\\{name}{today}.csv',"w+b") as csv: #creamos el archivo vacio y lo escribimos
            for i in link_to_dowload.iter_content(chunk_size=1024): #escribimos nuestro archivo
                if i:
                    csv.write(i)

    logging.debug(f'Se descargaron los archivos y se crearon las carpetas correctamente.')

except Exception as e:
    logging.exception(f'Hubo una excepcion: {e}')


for i,k in dirs_dict.items(): 
        if i == 'bibliotecas':
            df = pd.read_csv(k,sep=',', header=0,encoding='UTF-8')
            df = df.rename(configdf.bibliotecasRename,axis=1)
            df.astype({'web': 'object'}).dtypes
            df['año_inicio'] = df['año_inicio'].fillna(0)
            df['año_inicio'] = df['año_inicio'].round(decimals=0).astype(int)
            df.loc[df.año_inicio==0,'año_inicio']='s/d'
            df = df.fillna('s/d')
            df.drop_duplicates()
            df.to_csv(k, index=None)

        elif i == 'cines':
            df = pd.read_csv(k,sep=',', header=0,encoding='UTF-8')
            df = df.rename(configdf.cinesRename,axis=1)
            df['espacio_INCAA'] = df['espacio_INCAA'].fillna('no')
            df.loc[df.espacio_INCAA==0, 'espacio_INCAA'] = 'no'
            df = df.fillna('s/d')
            df.drop_duplicates()
            df.replace('0','no')
            df.to_csv(k, index=None)
    
        else:
            i == 'museos'
            df = pd.read_csv(k,sep=',', header=0,encoding='UTF-8')
            df = df.rename(configdf.museosRename,axis=1)
            df['año_inauguracion'] = df['año_inauguracion'].fillna(0)
            df['año_inauguracion'] = df['año_inauguracion'].round(decimals=0).astype(int)
            df.loc[df.año_inauguracion==0,'año_inauguracion']='s/d'
            df = df.fillna('s/d')
            df.drop_duplicates()
            df = df.fillna('s/d')
            df.to_csv(k, index=None)

logging.debug(f'Se renombraron y filtraron los data frames.')

for i,k in dirs_dict.items(): 
    models.push(i,k)
logging.debug(' Se cargaron los datos a la DB')

models.create_tables()
logging.debug(' Se crearon las tablas en la DB')
