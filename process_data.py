import pandas as pd


def limpieza():
    df_bibliotecas = pd.read_csv('datos/bibliotecas/2022-05/bibliotecas-09-05-2022.csv',sep=',', header=0)
    df_bibliotecas = df_bibliotecas.rename({'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia','IdDepartamento':'id_departamento','Categoría':'categoria','Provincia':'provincia','Localidad':'localidad','Nombre':'nombre','Domicilio':'domicilio',
                                               'CP':'codigo_postal','Teléfono':'numero_de_telefono','Mail':'mail','Web':'web',},axis=1)
    df_bibliotecas.astype({'web': 'object'}).dtypes
    df_bibliotecas['año_inicio'] = df_bibliotecas['año_inicio'].fillna(0)
    df_bibliotecas['año_inicio'] = df_bibliotecas['año_inicio'].round(decimals=0).astype(int)
    df_bibliotecas.loc[df_bibliotecas.año_inicio==0,'año_inicio']='s/d'
    df_bibliotecas = df_bibliotecas.fillna('s/d')
    df_bibliotecas.drop_duplicates()
    df_bibliotecas.to_csv('datos/bibliotecas/2022-05/bibliotecas-09-05-2022.csv', index=None)

    df_cines = pd.read_csv('datos/cines/2022-05/cines-09-05-2022.csv',sep=',',header=0) 
    df_cines.rename(columns={'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia','IdDepartamento':'id_departamento','Categoría':'categoria',
        'Provincia':'provincia','Localidad':'localidad','Nombre':'nombre','Dirección':'domicilio',
        'CP':'código_postal','Teléfono':'numero_de_telefono','Mail':'mail','Web':'web'},inplace=True)
    df_cines['espacio_INCAA'] = df_cines['espacio_INCAA'].fillna('no')
    df_cines.loc[df_cines.espacio_INCAA==0, 'espacio_INCAA'] = 'no'
    df_cines = df_cines.fillna('s/d')
    df_cines.drop_duplicates()
    df_cines.replace('0','no')
    df_cines.to_csv('datos/cines/2022-05/cines-09-05-2022.csv', index=None)
    
    df_museos = pd.read_csv('datos/museos/2022-05/museos-09-05-2022.csv',sep=',',header=0)
    df_museos.rename(columns={'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia','IdDepartamento':'id_departamento','categoria':'categoria',
        'Provincia':'provincia','Localidad':'localidad','Nombre':'nombre','direccion':'domicilio',
        'CP':'codigo_postal','telefono':'numero_de_telefono','Mail':'mail','Web':'web'},inplace=True)
    df_museos['año_inauguracion'] = df_museos['año_inauguracion'].fillna(0)
    df_museos['año_inauguracion'] = df_museos['año_inauguracion'].round(decimals=0).astype(int)
    df_museos.loc[df_museos.año_inauguracion==0,'año_inauguracion']='s/d'
    df_museos = df_museos.fillna('s/d')
    df_museos.drop_duplicates()
    df_museos = df_museos.fillna('s/d')
    df_museos.to_csv('datos/museos/2022-05/museos-09-05-2022.csv', index=None)

