#!/usr/bin/env python
# coding: utf-8

# # NSF CyberTraining Bootcamp, Friday (Intro to ML)

# ## 1. import basic libraries

# In[65]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import requests


# ## 1.a Downloading Data needed

# In[66]:


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

# In[67]:


df_train = pd.read_csv('data_train.csv')

print("length:",len(df_train))
df_train.head()


# ## 3. split data by feature and target

# In[68]:


X=df_train.iloc[:,:26]
X.head()


# In[69]:


Y=df_train["location"]
Y.head()


# In[70]:


collections.Counter(Y)


# In[ ]:





# In[ ]:





# ## 4. train KNN and decision tree model

# In[71]:


from sklearn import tree, neighbors


# In[72]:


model1=tree.DecisionTreeClassifier()
model2=neighbors.KNeighborsClassifier(n_neighbors=1)


# In[73]:


model1.fit(X,Y)
model2.fit(X,Y)


# ## 5. cross validate your training

# In[74]:


from sklearn.model_selection import cross_validate


# In[75]:


model1_cv=cross_validate(model1, X, Y, scoring='precision_macro', cv=5, return_train_score=False)
model2_cv=cross_validate(model2, X, Y, scoring='precision_macro', cv=5, return_train_score=False)


# In[76]:


model1_cv['test_score']


# In[77]:


print('decision tree', np.mean(model1_cv['test_score']))
print('knn', np.mean(model2_cv['test_score']))


# ## 6. tune KNN model

# In[78]:


from sklearn.model_selection import GridSearchCV


# In[79]:


parameters={'n_neighbors':range(1,1001,10)}
model2_GS = GridSearchCV(model2, parameters, cv=5, scoring='precision_macro', return_train_score=False)
model2_GS.fit(X,Y)


# In[80]:


model2_GS.cv_results_['params']


# In[81]:


model2_GS.cv_results_['mean_test_score']


# In[82]:


plt.scatter(x=range(1,1001,10), y=model2_GS.cv_results_['mean_test_score'])


# In[83]:


model2_GS.best_params_


# In[84]:


model2_GS.best_score_


# In[85]:


model2_GS.best_estimator_


# ## 7. test your model

# In[86]:


test=pd.read_csv('data_test.csv')


# In[95]:


test.head()


# In[88]:


len(test)


# In[89]:


X_test=test.iloc[:,:26]
Y_test=test['location']


# ## 8. report your result

# In[90]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[91]:


original_model=model2.predict(X_test)
tuned_model=model2_GS.predict(X_test)


# In[92]:


print('original Knn', accuracy_score(Y_test, original_model))


# In[93]:


cm=confusion_matrix(Y_test, original_model)
print(cm)


# In[94]:


print('Tuned Knn (k=391)', accuracy_score(Y_test, tuned_model))


# In[96]:


cm=confusion_matrix(Y_test, tuned_model)
print(cm)


# In[ ]:




