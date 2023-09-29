#!/usr/bin/env python
# coding: utf-8

# Merging af csv-filer fb_posts og population_pol

# In[6]:


import pandas as pd

file_path = r"C:\Users\Bruger\OneDrive\Skrivebord\Data DBeaver\population_pol_202309221442.csv"

fb1 = pd.read_csv(file_path)


# In[7]:


file_path = r"C:\Users\Bruger\OneDrive\Skrivebord\Data DBeaver\fb_posts_202309281304 behandlet komma.csv"

fb2 = pd.read_csv(file_path)


# In[8]:


fb2.head(10)


# In[15]:


columns_to_keep=[3,5,6,7,8]
fb2_kort=fb2.iloc[:, columns_to_keep]


# In[16]:


fb2_kort.head(10)


# In[17]:


fb1.head(10)


# In[19]:


merged_fb = pd.merge(fb1, fb2_kort, on='page_id')


# In[21]:


merged_fb.sample(10)


# In[22]:


merged_fb['party'].unique()


# In[23]:


merged_fb


# In[27]:


fb1['party'].unique()


# In[28]:


fb1_kopi = fb1.copy()


# In[29]:


columns_to_keep2=[4]
fb1_kopi=fb1_kopi.iloc[:, columns_to_keep2]


# In[32]:


fb1_kopi


# In[34]:


merged_fb.to_csv('fejlet_csv', index=False)


# In[ ]:




