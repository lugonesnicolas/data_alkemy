from sqlalchemy import create_engine 
from sqlalchemy import text

engine=create_engine("postgresql://postgres:4234@localhost:5432/Alkemy_Challenge", echo=False) #creamos la ruta de coneccion con la base de datos

"""Nos conectamos a la base de datos, abrimos el script .sql que contiene nuestras querys, codificamos con text para poder hacer uso de nuestro orm
y ejecutamos nuestros querys"""
with engine.connect() as con:
    with open("tables.sql", mode="r") as file:
        tables = text(file.read())
        con.execute(tables)