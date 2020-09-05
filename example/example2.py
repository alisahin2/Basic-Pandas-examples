#!/usr/bin/env python
# coding: utf-8

# In[160]:


import numpy as np
import pandas as pd


# In[165]:


salaryTable = {
    "Name" : [ "Hans", "Anna", "John", "Mohammed"],
    "Job" : ["Computer Engineer", "Fashion designer", "Jeweller ", "Cook"],
    "Salary($)" : [5000, 4500,10000,3500]
}


# In[166]:


salaryDf = pd.DataFrame(salaryTable)
salaryDf


# In[167]:


## get uniques
salaryDf["Job"].unique()


# In[168]:


salaryDf["Job"].nunique()


# In[169]:


salaryDf["Job"].value_counts()


# In[172]:


def netSalary(salary):
    return salary * 0.67


# In[173]:


salaryDf["Salary($)"].apply(netSalary)


# In[174]:


salaryDf.isnull()


# In[ ]:





# In[ ]:




