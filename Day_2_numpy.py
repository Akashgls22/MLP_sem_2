#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


np.zeros(3)


# In[6]:


a=[1,2,3]
print(a)


# In[33]:


b=([(1,7,9,4),(5,0,2,4),(3,4,5,6),(1,3,7,2)])
type(b)


# In[9]:


c=np.array(b)
print(c)


# In[10]:


np.zeros(3)


# In[11]:


np.zeros((2,3))


# In[12]:


np.zeros((3,2,4))


# In[13]:


np.full((3,4),2)


# In[15]:


np.random.rand(3,5)


# In[18]:


np.ones((3,4))


# In[19]:


np.eye(4)


# In[21]:


np.copy(c)


# In[35]:


c.view()


# In[37]:


c.sort()
c


# In[44]:


a1=c.reshape(4,-3)
print(a1)


# In[45]:


np.append(c,2)


# In[46]:


np.insert(c,4,3)


# In[51]:


b=np.delete(c,2)
print(b)


# In[53]:


a=np.delete(c,3)
print(a)


# In[ ]:




