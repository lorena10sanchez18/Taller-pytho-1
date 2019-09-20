#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pymysql
import pandas as pd # importat la libreria pandas como pd
import numpy as np 
import matplotlib.pyplot as plt
import os


# In[108]:


#Establecemos la conexion con la base de datos
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
databese = os.getenv('MYSQL_DATABASE')

#Conexion 
conexion = pymysql.connect (
    host = host,
    port = int(3306),
    user = "root",
    passwd = "",
    db = "consulta",
    charset ='utf8mb4')

resultado = pd.read_sql_query("SELECT * FROM cliente",conexion)
resultado.tail(10)


# In[109]:


resultado.columns


# In[110]:


resultado.head()


# In[111]:


resultado = resultado.dropna(subset=["direccion"])


# In[113]:


resultado.dropna()


# In[114]:


resultado.describe()


# In[ ]:





# In[116]:


resultado = resultado.fillna(resultado.mean())


# In[117]:


resultado


# In[119]:


edad = resultado.edad
plt.plot(edad)
plt.show()


# In[ ]:




