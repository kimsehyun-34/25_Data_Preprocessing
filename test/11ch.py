#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pandas')


# In[5]:


import pandas as pd


# In[88]:


df=pd.read_csv("C:/Users/User/Downloads/Data_Sample.csv")


# In[89]:


df


# In[90]:


df.isnull().sum() #1


# In[91]:


df = df.rename(columns={ #2
    'Value1': 'A',
    'Value2': 'B',
    'Value3': 'C'
})
df


# In[92]:


df["A"]


# In[93]:


categorical_columns = df.select_dtypes(include=['object']).columns #3
numerical_columns = df.select_dtypes(include=['number']).columns

df_categorical = df[categorical_columns]
df_numerical = df[numerical_columns]

columns_to_fill = ['A', 'B', 'C']
df[columns_to_fill] = df[columns_to_fill].fillna(df[columns_to_fill].median())
df_combined.head()


# In[94]:


df_combined = pd.concat([df_numerical, df_categorical], axis=1) #4
df_combined.head()


# In[95]:


df['Total'] = df['A'] + df['B'] + df['C'] #5
df = df.drop(columns=['A', 'B', 'C'])

df.head()


# In[96]:


df[['Model', 'Serial']] = df['Model_Serial'].str.split('-', expand=True) #6
df = df.drop(columns=['Model_Serial'])
df


# In[75]:


df['Model'].value_counts()#7


# In[72]:


df['Model'] = df['Model'].replace({" Alpha": "Alpha"})
df['Model'] = df['Model'].replace({"AIpha": "Alpha"})
df['Model'] = df['Model'].replace({" Beta": "Beta"})
df['Model'] = df['Model'].replace({"Gamma ": "Gamma"})

df['Model_Serial'] = df['Model'] + '-' + df['Serial']


# In[74]:


df['Model'].unique()


# In[73]:


df


# In[85]:


#==== 7 다른방식
df['Model'].value_counts()


# In[86]:


df['Model'] = df['Model'].replace({
    " Alpha": "Alpha",
    "AIpha": "Alpha",
    " Beta": "Beta",
    "Gamma ": "Gamma"
})

df['Model_Serial'] = df['Model'] + '-' + df['Serial']


# In[87]:


df['Model'].value_counts()


# In[97]:


#===== 
df['Model'].value_counts()


# In[98]:


df = pd.DataFrame({
    'Model': ['value1-value2-value3', ‘value1-value4-value5’, ‘vvdfvalue1']
})


# In[ ]:




