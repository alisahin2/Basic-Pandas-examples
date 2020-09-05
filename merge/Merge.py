#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


group1 = { "Name" : [ "Hans", "Anna", "John", "Mohammed","Tom"],
             "Job" : ["Computer Engineer", "Fashion designer", "Gardener ", "Jeweller ", "Cook"]}


# In[4]:


mergeDf1 = pd.DataFrame(group1)
mergeDf1


# In[5]:


group2 = { "Name" : [ "Hans", "Anna", "John", "Mohammed","Tom"],
             "Car" : ["Daimler", "Ford", "Nissan ", "Audi ", "Mazda"]}


# In[6]:


mergeDf2 = pd.DataFrame(group2)
mergeDf2


# In[7]:


pd.merge(mergeDf1, mergeDf2, on = "Name")

