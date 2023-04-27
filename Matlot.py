#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


x=np.linspace(0,100,10)
y=x*x


# In[3]:


plt.plot(x,y)


# In[5]:


x=['A','B','C']
y=[50,70,90]
print('x=:',x)
print('y=:',y)
plt.title('Line Chart Demo')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.plot(x,y)


# In[6]:


X=np.linspace(0,10,100)
Y=np.sin(X)
plt.plot(X,Y)


# In[7]:


Y2=np.cos(X)
plt.plot(X,Y2)


# In[9]:


#Bar Chart 
x=np.array(['A','B','C','D'])
y=np.array([3,8,1,10])
plt.bar(x,y)


# In[10]:


#BarH
plt.barh(x,y)


# In[15]:


categories=np.array(['A','B','C','D'])
values1=np.array([3,8,1,10])
values2=np.array([6,2,7,5])
bar_width=0.35

plt.bar(categories,values1,bar_width,label='Dataset1')
plt.bar(categories,values2,bar_width+0.20,label='Dataset2')

plt.title('Grouped Bar Chart Example')
plt.legend()
plt.show()


# In[16]:


categories=np.array(['A','B','C','D'])
values=np.array([3,8,1,10])

plt.pie(values, labels=categories)

plt.title('Simple Pie Chart Example')
plt.show()


# In[19]:


#explor 
explode=(0.1,0,0,0)
plt.pie(values, labels=categories, explode=explode, autopct='%1.f%%')
plt.show()


# In[22]:


item=np.array(['Electronics','Clothing','Grocery','Household'])
sell=np.array([5000,6000,4000,3500])
e=(0,0.1,0,0)
plt.pie(sell, labels=item, explode=e, autopct='%1.f%%')
plt.show()

plt.bar(item,sell)


# In[ ]:




