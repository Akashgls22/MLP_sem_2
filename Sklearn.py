#!/usr/bin/env python
# coding: utf-8

# In[15]:


#sklearn- Lab1
# Linear Regression Model
import pandas as pd
import numpy as np


# In[2]:


df= pd.read_csv('Desktop/iris.csv')
df


# In[16]:


df['variety'].value_counts()


# In[17]:


x=df.iloc[:,0:4].values # filter Independent variable
 
y=df.iloc[:,4].values  # filter dependent variable


# In[18]:


from sklearn.preprocessing import LabelEncoder


# In[19]:


labelencoder_y= LabelEncoder()
y=labelencoder_y.fit_transform(y)
y


# In[20]:


from sklearn.model_selection import train_test_split 
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
x_train


# In[21]:


x_train.size


# In[22]:


x_test.size


# In[23]:


y_train.size


# In[24]:


y_test.size


# In[25]:


from sklearn.linear_model import LogisticRegression


# In[26]:


logmodel=LogisticRegression()
logmodel.fit(x_train,y_train)


# In[27]:


y_pred= logmodel.predict(x_test)
y_pred
np.sort(y_pred)


# In[28]:


y_test
np.sort(y_test)


# In[29]:


from sklearn.metrics import confusion_matrix


# In[30]:


confusion_matrix(y_test,y_pred)


# In[31]:


(28/30)*100


# In[32]:


logmodel.score(x_test,y_test)


# In[33]:


from sklearn.neighbors import KNeighborsClassifier


# In[34]:


classifier_knn= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2) # distance name
classifier_knn.fit(x_train,y_train) # model training 70:30


# In[44]:


y_pred_knn=classifier_knn.predict(x_test)
y_pred_knn


# In[39]:


from sklearn.metrics import confusion_matrix


# In[45]:


confusion_matrix(y_test,y_pred_knn)


# In[46]:


classifier_knn.score(x_test,y_test)


# In[47]:


from sklearn.metrics import accuracy_score
accuracy_score(y_pred_knn,y_test)


# In[5]:


# NaiveBias Model
from sklearn.naive_bayes import GaussianNB


# In[34]:


classifier_nb= GaussianNB()


# In[36]:


classifier_nb.fit(x_train,y_train)


# In[37]:


y_pred= classifier_nb.predict(x_test)
y_pred


# In[48]:


from sklearn.metrics import accuracy_score
accuracy_score(y_pred_knn,y_test)


# In[ ]:


confusion_matrix(y_test,y_pred)


# In[40]:


classifier_nb.score(x_test,y_test)


# In[ ]:




