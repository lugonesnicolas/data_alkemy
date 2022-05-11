import pandas as pd
from main import dirs_dict
import configdf


def limpieza():
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



