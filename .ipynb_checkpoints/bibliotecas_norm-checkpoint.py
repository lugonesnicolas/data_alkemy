#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd


# In[43]:


df_bibliotecas = pd.read_csv('datos/bibliotecas/2022-05/bibliotecas-08-05-2022.csv',sep=',', header=0)


# In[44]:


df_bibliotecas


# In[45]:


df_bibliotecas.columns


# In[46]:


df_bibliotecas = df_bibliotecas.rename({'Cod_Loc':'cod_localidad','IdProvincia':'id_provincia','IdDepartamento':'id_departamento','Categoría':'categoria','Provincia':'provincia','Localidad':'localidad','Nombre':'nombre','Domicilio':'domicilio',
                                               'CP':'codigo postal','Teléfono':'numero de telefono','Mail':'mail','Web':'web',},axis=1)


# In[47]:


df_bibliotecas.head()


# In[48]:


df_bibliotecas.info()


# In[49]:


df_bibliotecas.astype({'web': 'object'}).dtypes


# In[50]:


df_bibliotecas.drop_duplicates()


# In[51]:


df_bibliotecas['año_inicio'] = df_bibliotecas['año_inicio'].fillna(0)


# In[52]:


df_bibliotecas['año_inicio'] = df_bibliotecas['año_inicio'].round(decimals=0).astype(int)


# In[53]:


df_bibliotecas.loc[df_bibliotecas.año_inicio==0,'año_inicio']='s/d'


# In[54]:


df_bibliotecas = df_bibliotecas.fillna('s/d')


# In[55]:


df_bibliotecas.head()


# In[56]:


df_bibliotecas.to_csv('datos/bibliotecas/2022-05/bibliotecas-08-05-2022.csv', index=None)

