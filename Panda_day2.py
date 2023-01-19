#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


mdf=pd.read_csv('Movie-Data.csv')
mdf


# In[5]:


mdf.shape


# In[6]:


mdf.head(10)


# In[7]:


mdf.tail(10)


# In[8]:


mdf.info()


# In[9]:


mdf.describe()


# In[10]:


clist=mdf.columns
clist


# In[12]:


mdf=pd.read_csv('Movie-Data.csv',index_col='Title')
mdf


# In[13]:


mdf.isnull()


# In[14]:


mdf.isnull().sum()


# In[15]:


mdf['Revenue (Millions)']


# In[16]:


r=mdf['Revenue (Millions)']
r


# In[17]:


type(r)


# In[22]:


rmean=r.mean()
rmean


# In[21]:


r2=mdf[['Revenue (Millions)','Year']]
r2


# In[20]:


type(r2)


# In[25]:


r.fillna(rmean,inplace=True)
r


# In[26]:


mdf.info()


# In[27]:


#Extract metascore
m=mdf['Metascore']
m


# In[28]:


m.isnull().sum()


# In[29]:


m.mean()


# In[30]:


mmean=m.mean()
mmean


# In[31]:


m.fillna(mmean,inplace=True)
m


# In[32]:


mdf.info()


# In[33]:


import pandas as pd


# In[34]:


df=pd.read_csv('movie-data.csv')
df


# In[35]:


df.info()


# In[ ]:




