import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy import text

engine=create_engine("postgresql://postgres:4234@localhost:5432/Alkemy_Challenge", echo=False) #creamos la ruta de coneccion con la base de datos

"""Nos conectamos a la base de datos, abrimos el script .sql que contiene nuestras querys, codificamos con text para poder hacer uso de nuestro orm
y ejecutamos nuestros querys"""


def push(name: str,path: str):
    if name == 'bibliotecas':
        with engine.connect() as con:
            df = pd.read_csv(path,sep=',', header=0,encoding='UTF-8')
            df.to_sql(
                name="bibliotecas",
                con=engine,
                index=False,
                if_exists="replace",
            )
        
    elif name == 'cines':
            with engine.connect() as con:
                df = pd.read_csv(path,sep=',', header=0,encoding='UTF-8')
                df.to_sql(
                name="cines",
                con=engine,
                index=False,
                if_exists="replace",
            )

    else:
        with engine.connect() as con:
            name == 'museos'
            df = pd.read_csv(path,sep=',', header=0,encoding='UTF-8')
            df.to_sql(
                name="museos",
                con=engine,
                index=False,
                if_exists="replace",
            )

def create_tables():
    with engine.connect() as con:
        with open("tables.sql", mode="r") as file:
            tables = text(file.read())
            con.execute(tables)



