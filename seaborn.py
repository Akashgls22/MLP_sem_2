#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns


# In[10]:


import matplotlib.pyplot as plt


# In[29]:


import pandas as pd


# In[2]:


print(sns.get_dataset_names())


# In[3]:


df=sns.load_dataset('titanic')
df


# In[4]:


df.info()


# In[16]:


iris=sns.load_dataset('iris')
iris


# In[18]:


plt.plot(iris['petal_length'],iris['sepal_length'])


# In[19]:


iris.plot(kind='scatter',
        x='petal_length',
        y='sepal_length') #Grid
plt.grid()
plt.show()


# In[21]:


sns.set(style='darkgrid')#whitegrid
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)


# In[23]:


sns.FacetGrid(iris,hue='species',height=6).map(plt.scatter,'sepal_length','petal_length').add_legend()


# In[31]:


data=pd.read_csv('Desktop/census_data.csv')
data


# In[32]:


sns.relplot(x="capital_loss",y="capital_gain",hue='marital_status',size='age',data=data)


# In[34]:


sns.catplot(x="age",y="marital_status",kind="box",hue='gender',data=data)


# In[35]:


sns.catplot(x="age",y="marital_status",kind="violin",hue='gender',data=data)


# In[36]:


sns.catplot(x="marital_status",kind="count",hue='gender',data=data)


# In[ ]:




