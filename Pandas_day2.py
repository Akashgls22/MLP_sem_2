#!/usr/bin/env python
# coding: utf-8

# In[2]:


names=['Akash','Pratik','Jaymin','Trup']
names


# In[3]:


marks=[40,50,60,60]
marks


# In[4]:


type(marks)


# In[5]:


import pandas as pd


# In[6]:


df=pd.Series(data=marks)


# In[7]:


df


# In[8]:


type(df)


# In[10]:


cf=pd.Series(data=names)


# In[11]:


cf


# In[12]:


student={'names':names,'marks':marks}
student


# In[13]:


type(student)


# In[14]:


df=pd.DataFrame(data=student)


# In[15]:


df


# In[16]:


df.shape


# In[17]:


df.info


# In[18]:


df.describe


# In[19]:


df.head()


# In[20]:


df.head(2)


# In[21]:


df.tail()


# In[22]:


df.tail(2)


# In[26]:


df=pd.read_csv('student1.csv')
df


# In[27]:


df.head(2)


# In[28]:


df.columns


# In[31]:


df['Name']


# In[32]:


df.info


# In[33]:


df.describe


# In[34]:


df.iloc[2]


# In[35]:


df.iloc[1:4]


# In[36]:


df.tail(3)


# In[37]:


df.head(3)


# In[38]:


df=pd.read_csv('panda_homework.csv')
df


# In[ ]:




