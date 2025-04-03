#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=
b=
print(a+b)


# In[ ]:


name = "김세현"
print("저의 이름은 {} 입니다..".format(name))


# In[1]:


get_ipython().system('pip install numpy')


# In[38]:


import numpy as np
a=[1,5,5,7,3,6,88,12,5,74,4,8,64,2,7,89,33,1,6,8,1,5,6,7]
b=np.array(a)

print(a)
print(b)


# In[40]:


print(b[0:5])
print(b[5:10])


print(b[0:5] + b[5:10])


# In[13]:


print(a.index(88)) 


# In[23]:


name=["Jone-30", "Park-30", "Kim-20", "Lee-10", "Oh-32", "Kang-25"]


print("결과1:{}".format(name[3][:name[3].index("-")]))


# In[36]:


l = ["데이터 전처리 수업, 입니다", "Data Preprocesing"]

l.pop(0)
l.append("데이터 전처리 수업 입니다")

l.pop(0)
l.append("Data preprocesing")

print("결과1:{}".format(l[0]))
print("결과2:{}".format(l[1]))


# In[ ]:




