#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


data= pd.read_csv('Desktop/iris.csv')
data


# In[4]:


data.head(10)


# In[5]:


data.info()


# In[6]:


x=data.iloc[:,0:4].values
x


# In[7]:


x.shape


# In[8]:


y=data.iloc[:,4].values
y


# In[9]:


y.shape


# In[10]:


from sklearn.preprocessing import LabelEncoder
label_encoder_y= LabelEncoder()
y= label_encoder_y.fit_transform(y)
y


# In[11]:


from sklearn.svm import SVC


# In[12]:


classifier_svc_sig = SVC(kernel = 'sigmoid') # rbf, linear,poly
classifier_svc_sig


# In[13]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=  train_test_split(x,y, test_size=0.5)
classifier_svc_sig.fit(x_train,y_train)


# In[14]:


y_pred= classifier_svc_sig.predict(x_test)
y_pred


# In[15]:


y_test


# In[16]:


from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)


# In[17]:


classifier_svc_sig.score(x_test,y_test)


# In[ ]:




