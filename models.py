import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy import text

engine=create_engine("postgresql://postgres:4234@localhost:5432/Alkemy_Challenge", echo=False) #creamos la ruta de coneccion con la base de datos

"""Nos conectamos a la base de datos, abrimos el script .sql que contiene nuestras querys, codificamos con text para poder hacer uso de nuestro orm
y ejecutamos nuestros querys"""


def bibliotecas_push():
    with engine.connect() as con:
        df_data_norm = pd.read_csv("datos/bibliotecas/2022-05/bibliotecas-09-05-2022.csv", sep=",", header=0) 
        df_data_norm.to_sql(
            name="bibliotecas",
            con=engine,
            index=False,
            if_exists="replace",
        )

def cines_push():
    with engine.connect() as con:
        df_data_norm = pd.read_csv("datos/cines/2022-05/cines-09-05-2022.csv", sep=",", header=0) 
        df_data_norm.to_sql(
            name="cines",
            con=engine,
            index=False,
            if_exists="replace",
        )

def museos_push():
    with engine.connect() as con:
        df_data_norm = pd.read_csv("datos/museos/2022-05/museos-09-05-2022.csv", sep=",", header=0) 
        df_data_norm.to_sql(
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


def create():
    bibliotecas_push()
    cines_push()
    museos_push()
    create_tables()
