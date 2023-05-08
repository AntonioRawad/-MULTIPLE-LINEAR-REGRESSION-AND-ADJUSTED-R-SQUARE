#!/usr/bin/env python
# coding: utf-8

# # MULTIPLE LINEAR REGRESSION AND ADJUSTED R SQUARE 

# # IMPRT RELIVANT LIBRARIES 

# In[ ]:





# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
seaborn.set()


# # LOAD THE DATA 

# In[4]:


data = pd.read_csv('C:/Users/rawad/OneDrive/Desktop/aws Restart course/Udemy Data Science Course/exercise/1.02.+Multiple+linear+regression.csv')


# In[ ]:





# In[7]:


data

# new model college GPA= b0+b1SAT+b2Rand1.2.3 (the randum value added to each student )
# In[8]:


data.describe()


# In[11]:


y = data['GPA']
x1 = data[['SAT', 'Rand 1,2,3']]
x = sm.add_constant(x1)

results = sm.OLS(y, x).fit()
print(results.summary())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




