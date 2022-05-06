import pandas as pd
from sqlalchemy import create_engine


engine=create_engine("postgresql://postgres:4234@localhost:5432/Alkemy_Challenge", echo=False)
df_data_norm = pd.read_csv("datos_procesados\data_norm.csv", sep=",", header=0) 
df_data_norm.to_sql(
    name="datos_normalizados",
    con=engine,
    index=False,
    if_exists="append"
)