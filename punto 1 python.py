#!/usr/bin/env python
# coding: utf-8

# In[41]:


#Integrantes
#Lorena Sanchez
#Elkin Ramirez
#Juan Felipe Marin 


# In[94]:


import pandas as pd # importat la libreria pandas como pd
import numpy as np 
import matplotlib.pyplot as plt
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.espn.com.co/futbol/posiciones/_/liga/COL.1/ordenar/wins/dir/desc")
bsObj = BeautifulSoup(html, "lxml")
table = bsObj.findAll("table",{"class":"Table2__table__wrapper"})[0]
rows = table.findAll("tr")
csvFile = open("tabla.csv", 'wt',newline= '')
writer = csv.writer(csvFile)

try: 
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()


# In[98]:


datos = pd.read_csv("tabla.csv") # cargar desde jupyter el archivo tabla.cvs


# In[81]:


datos


# In[76]:


datos.dropna()


# In[45]:


datos.head()


# In[47]:


DIF = datos.DIF
plt.plot(DIF)
plt.show()


# In[ ]:




