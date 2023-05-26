#!/usr/bin/env python
# coding: utf-8

# # NSF CyberTraining Bootcamp, Friday (Intro to ML)

# ## 1. import basic libraries

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import requests


# ## 1.a Downloading Data needed

# In[ ]:


repository_url = "https://raw.githubusercontent.com/stm5131/nsfcybertraining/main/Machine%20Learning%20-%20Friday%20Session/" 

files = ["data_all.csv","data_test.csv","data_train.csv"]

for filename in files:
    csv_url = repository_url+filename
    #print(csv_url)
    response = requests.get(csv_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f: 
            f.write(response.content) 
            print(filename + " downloaded successfully.")
    else: 
        print('Failed to download '+filename) 


# ## 2. read data

# In[ ]:





# In[ ]:





# In[ ]:





# ## 3. split data by feature and target

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 4. train KNN and decision tree model

# In[ ]:





# In[ ]:





# In[ ]:





# ## 5. cross validate your training

# In[ ]:





# In[ ]:





# In[ ]:





# ## 6. tune KNN model

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 7. test your model

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 8. report your result

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




