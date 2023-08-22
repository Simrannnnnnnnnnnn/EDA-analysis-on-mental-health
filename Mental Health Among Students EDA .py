#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[78]:


data = pd.read_csv("C:/Users/kaurs/Downloads/datasetMental/Student Mental health.csv", encoding="iso-8859-1", low_memory=False)


# In[79]:


data.head()


# In[80]:


data.tail()


# In[81]:


data.shape


# In[82]:


data.describe()


# In[83]:


data.columns


# In[84]:


data.nunique()


# In[85]:


data['What is your course?'].unique()


# In[86]:


data['Timestamp'].unique()


# In[87]:


data.isnull().sum()


# In[88]:


data[data['Age'].isnull()]


# In[89]:


data = data[-data['Age'].isnull()]


# In[90]:


data.Age.isnull().sum()


# In[91]:


data.isnull().sum()


# In[92]:


dp = data.drop(['Timestamp'],axis=1)


# In[93]:


dp.head()


# In[94]:


numerical_data = dp.select_dtypes(include=[np.number])
corelation= numerical_data.corr()


# In[95]:


plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Do you have Depression?', hue='Do you have Anxiety?')
plt.title('Distribution of Mental Health Conditions')
plt.xlabel('Depression')
plt.ylabel('Count')
plt.show()


# In[96]:


plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Choose your gender', hue='Do you have Depression?')
plt.title('Distribution of Mental Health Conditions by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[97]:


plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Your current year of Study', hue='Do you have Anxiety?')
plt.title('Distribution of Mental Health Conditions by Current Year of Study')
plt.xlabel('Current Year of Study')
plt.ylabel('Count')
plt.show()


# In[98]:


plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Marital status', hue='Do you have Panic attack?')
plt.title('Distribution of Mental Health Conditions by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()


# In[99]:


plt.figure(figsize=(8, 6))
data['Treatment'] = data['Did you seek any specialist for a treatment?'].apply(lambda x: 'Seek Treatment' if x == 'Yes' else 'No Treatment')
sns.countplot(data=data, x='Do you have Depression?', hue='Did you seek any specialist for a treatment?')
plt.title('Treatment Seeking Behavior for Depression')
plt.xlabel('Depression')
plt.ylabel('Count')
plt.show()


# In[100]:


mental_health_columns = ['Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?']
data[mental_health_columns] = data[mental_health_columns].apply(lambda x: x.map({'No': 0, 'Yes': 1}))

corr_matrix = data[mental_health_columns].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Mental Health Conditions')
plt.show()


# In[ ]:




