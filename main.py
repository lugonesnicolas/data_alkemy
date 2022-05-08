import logging
# import pandas
from multiprocessing.sharedctypes import Value
import os
import datetime
import requests
import logging
from bs4 import BeautifulSoup
import models
import process_data

logging.basicConfig(filename='main.log',level=logging.DEBUG)


"""Diccionario con los links que van a pasar a nuestra funcion"""
links_to_transform = {
    'museos' : 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/archivo/4207def0-2ff7-41d5-9095-d42ae8207a5d',
    'cines' : 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae',
    'bibliotecas' : 'https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_01c6c048-dbeb-44e0-8efa-6944f73715d7',
}

"""codificamos la hora para poder usarlas en la creacion de carpetas y archivos"""
today = datetime.date.today().strftime('-%d-%m-%Y')
year_month = datetime.date.today().strftime('%Y-%m') 

"""Funcion que toma el diccionario, toma los 2 items y los transforma en variables.
luego llama a la url con requests y la acomoda con BeautifulSoup, filtramos las etiquetas hasta encontrar nuestros links de descarga.
Hacemos uso de reques para descargar el link del archivo csv, definimos la ruta codificada con nombre y fecha, creamos el directorio, y los archivos correspondientes.
"""

def get_link():
    for k,v in links_to_transform.items():
        name = k
        url = v
        page = requests.get(url) #llamamos la pagina web
        soup = BeautifulSoup(page.content, 'html.parser') #acomodamos el request en el formato html
        get_links = soup.find("a", "btn btn-green btn-block") #filtramos la clase y etiqueta
        links = get_links.attrs.get('href') #filtramos el contenedor del link
        link_to_dowload = requests.get(links, stream = True) #leemos el link que contiene la descarga
        # c_subc = os.path.join("datos/",name,year_month,name + today) #creamos la ruta con nombre y fecha
        c_subc = os.path.join("datos/",name,year_month) #creamos la ruta con nombre y fecha
        os.makedirs(c_subc, exist_ok=True) #creamos el directorio
        with open(c_subc+f'/{name}{today}.csv',"w+b") as csv: #creamos el archivo vacio y lo escribimos
            for i in link_to_dowload.iter_content(chunk_size=1024): #escribimos nuestro archivo
                if i:
                    csv.write(i)
        logging.info('Corrio el programa sin fallas, chequear siempre las etiquetas html por si cambian')


def menu():
    print("Bienvenido a mi proyecto de  Data y Analytics de Alkemy")
    while True:  
        try:
            os.system("cls")
            seleccion = int(input("Selecciona: \n 1.Para descargar los archivos \n 2.Para procesar los datos \n 3.Para actualizar base de datos "))
            break
        except ValueError:
            print("Solo se puede ingresar a las opciones 1 y 2")

    if seleccion == 1:
            get_link()
    elif seleccion == 2:
        process_data.limpieza()
    elif seleccion == 3:
        models.create()
    else:
        print("Elegiste una opcion no valida")


def run():
    menu()
    # get_link()
    # models.create_base()


if __name__ == "__main__":
    run()