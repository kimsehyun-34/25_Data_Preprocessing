#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = [10, 20, 30, [1,2,3]]


# In[4]:


print(a[a.index([1,2,3])])


# In[5]:


수학 = [20,30,40,50,60]
영어 = [50,70,50,60,90]


# In[6]:


import re
b = "https://www.youtube.com/"

re.sub('www.youtube.com', 'www.naver.com', b)


# In[16]:


am = sum(m) / len(m)
ae = sum(e) / len(e)
print("수학평균: ",am)
print("영어평균: ",ae)


# In[23]:


import numpy as np

a6 = np.array([1,2,100,4,5,900])
a6 = np.delete(a6, 2)
a6 = np.delete(a6, -1)
print(a6)


# In[31]:


ds = {"수학점수":[20,30,40,50,60],"영어점수":[50,70,50,60,90]}

print(ds["수학점수"][0]+ds["영어점수"][0])


# In[33]:





# In[ ]:




