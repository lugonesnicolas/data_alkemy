import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy import text

engine=create_engine("postgresql://postgres:4234@localhost:5432/Alkemy_Challenge", echo=False) #creamos la ruta de coneccion con la base de datos

"""Nos conectamos a la base de datos, abrimos el script .sql que contiene nuestras querys, codificamos con text para poder hacer uso de nuestro orm
y ejecutamos nuestros querys"""
with engine.connect() as con:
    with open("tables.sql", mode="r") as file:
        tables = text(file.read())
        con.execute(tables)

# with engine.connect() as con:
#     df_data_norm = pd.read_csv("datos_norm\data_norm.csv", sep=",", header=0) 
#     df_data_norm.to_sql(
#         name="datos_norm",
#         con=engine,
#         index=False,
#         if_exists="replace",
#     )

# with engine.connect() as con:
#     df_cines_count = pd.read_csv("datos_norm\cines_count.csv", sep=",", header=0)
#     df_data_norm.to_sql(
#         name="cines_count",
#         con=engine,
#         index=False,
#         if_exists="replace",
#     )