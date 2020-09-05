#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[9]:


katalog1 = { "Isim" : [ "Ali", "Emre", "Merve", "Semih","Ayse"],
             "Sehir" : ["Eskisehir", "Ankara", "Kutahya", "Seattle", "Adana"],
             "Plaka" : [26, 6, 43, 82, 1]}


# In[12]:


df1 = pd.DataFrame(katalog1, index = [0,1,2,3,4])
df1


# In[18]:


katalog2 = { "Isim" : [ "Leyla", "Metin", "Kerim", "Selman", "Selim"],
             "Sehir" : ["Eskisehir", "Kutahya", "Adana", "Las Vegas", "Frankfurt"],
             "Plaka" : [26, 43, 1, 83, 86]}


# In[20]:


df2 = pd.DataFrame(katalog2, index = [5,6,7,8,9])
df2


# In[21]:


katalog3 = { "Isim" : [ "Mecnun", "Merkel", "Sanna", "Anna", "Zehra"],
             "Sehir" : ["Eskisehir", "Frankfurt", "Helsinki", "Toronto", "Kutahya"],
             "Plaka" : [26, 86, 85, 84, 43]}


# In[22]:


df3 = pd.DataFrame(katalog3, index = [10,11,12,13,14])
df3


# In[23]:


pd.concat([df1, df2, df3])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




