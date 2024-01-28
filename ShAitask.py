#!/usr/bin/env python
# coding: utf-8

# # Basic Data Exploration

# In[2]:


# importing library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_csv("Salaries.csv" , sep = "," ,encoding = "utf-8")
data


# In[4]:


data.head()


# In[5]:


data.head(10)


# In[6]:


data.sample(20)


# In[7]:


data.shape


# In[8]:


data.size


# In[9]:


data.info()


# In[10]:


data.columns


# In[11]:


data.columns.to_list()


# In[12]:


Categorical=data.select_dtypes(include='object').columns.tolist()
Categorical


# In[13]:


Numerical=data.select_dtypes(exclude='object').columns.tolist()
Numerical


# # Data Cleaning

# In[16]:


data.isnull()


# In[17]:


data.isnull().sum().sort_values()


# In[18]:


sns.heatmap(data.isnull())


# In[19]:


data_new=data.copy()


# In[20]:


data_new= data_new.drop(['Id'], axis=1)


# In[21]:


data_new= data_new.drop(['Notes','Status'], axis=1)
data_new.head()


# In[22]:


data_new["Benefits"]


# In[23]:


sns.kdeplot(data_new["Benefits"], shade=True, bw=0.5, color="olive")
plt.show()


# In[24]:


data_new["Benefits"]=data_new["Benefits"].fillna(data_new["Benefits"].mean())


# In[25]:


sns.kdeplot(data_new["Benefits"], shade=True, bw=0.5, color="olive")
plt.show()


# In[26]:


sns.kdeplot(data_new["BasePay"], shade=True, bw=0.5, color="green")
plt.show()


# In[27]:


data_new["BasePay"]=data_new["BasePay"].fillna(data_new["BasePay"].median())


# In[28]:


sns.kdeplot(data_new["BasePay"], shade=True, bw=0.5, color="green")
plt.show()


# In[29]:


data_new.isnull().sum().sort_values()


# In[30]:


data_new.dropna(inplace=True)


# In[31]:


data_new.isnull().sum().sum()


# In[32]:


data_new[data_new.duplicated()]


# # Descriptive Statistics

# In[33]:


data_new.describe().T.style.background_gradient(cmap='YlOrRd')


# In[34]:


data_new.describe()[1:].T.style.background_gradient(cmap='YlOrRd')


# In[35]:


data_new.describe(percentiles=[.25,.5,.75,.90,.95,.99])[1:].T.style.background_gradient(cmap='YlOrRd')


# In[14]:


data["TotalPay"].agg(["min" , 'max' , 'mean' , "std"])


# # Simple Correlation Analysis
# 

# In[36]:


sns.heatmap(data_new.corr(),annot=True)


# In[37]:


sns.pairplot(data_new)


# In[38]:


data_new["TotalPay"].value_counts()


# # Basic Data Visualization

# In[39]:


plt.hist(data_new["TotalPay"])


# In[40]:


data_new["JobTitle"].value_counts()


# In[103]:


top_10_job_titles = data_new['JobTitle'].value_counts().head(10)

# Create a pie chart
plt.pie(top_10_job_titles.values, labels=top_10_job_titles.index, autopct="%1.1f%%")  # Show percentages
plt.title("Top 10 Job Titles")
plt.show()


# In[41]:


data_new["EmployeeName"].value_counts()


# In[42]:


data_new["Agency"].value_counts()


# In[43]:


data_new["JobTitle"].dtypes


# In[44]:


sns.kdeplot(data=data_new, x="TotalPay")


# # Grouped Analysis

# In[45]:


data_new.groupby(["TotalPay"]).sum()


# In[46]:


data_new["Year"].value_counts()


# In[47]:


data_new['TotalPay'].agg(['min' , 'max'])


# In[89]:


data_new.groupby(["TotalPay"]).sum()[["Year"]]


# In[79]:


data_new[data_new['TotalPay'] >=142489.801000]['JobTitle'].value_counts()


# In[80]:


data_new['TotalPayBenefits'].agg(['min' , 'max'])


# In[85]:


data_new[data_new['TotalPayBenefits'] >=177087.470000]['JobTitle'].value_counts()


# In[49]:


import plotly.express as px
fig = px.scatter(data_new, x="TotalPay",y="Year")
fig.show()


# In[50]:


data_new.groupby(['JobTitle']).sum()[["TotalPay"]]


# In[93]:


data_new.groupby(['JobTitle']).max().sort_values("TotalPay" , ascending= False)[["TotalPay"]]


# In[98]:


data_new.groupby(['JobTitle']).min().sort_values("TotalPay" , ascending= False)[["TotalPay"]]


# In[94]:


import plotly.express as px
fig = px.scatter(data_new, x="TotalPay",y="JobTitle")
fig.show()


# In[95]:


data_new.groupby(['BasePay']).max().sort_values("TotalPay" , ascending= False)[["TotalPay"]]


# In[53]:


data_new.groupby(['BasePay']).mean().sort_values("TotalPay" , ascending= False)[["TotalPay"]]


# In[54]:


import plotly.express as px
fig = px.scatter(data_new, x="BasePay",y="TotalPay")
fig.show()


# In[55]:


data_new.groupby(['OvertimePay']).mean().sort_values("TotalPay" , ascending= False)[["TotalPay"]]


# In[56]:


import plotly.express as px
fig = px.scatter(data_new, x="OvertimePay",y="TotalPay")
fig.show()


# In[99]:


data_new.groupby(['Benefits']).mean().sort_values("Year" , ascending= False)[["BasePay","OvertimePay"]]


# In[100]:


import plotly.express as px
fig = px.scatter(data, x="BasePay", y="OvertimePay", color="TotalPay",
                 hover_data=['Benefits'])
fig.show()


# In[101]:


import plotly.express as px
fig = px.scatter(data_new, x="BasePay",y="Benefits")
fig.show()


# In[102]:


import plotly.express as px
fig = px.scatter(data_new, x="OvertimePay",y="TotalPayBenefits")
fig.show()


# In[96]:


data_new[['BasePay','OvertimePay']].corr()


# In[97]:


import plotly.express as px
fig = px.scatter(data_new, x="OvertimePay",y="BasePay")
fig.show()


# In[73]:


data_new['JobTitle'].value_counts().head(10).plot()
plt.xticks(rotation=45)


# In[72]:


data_new.loc[data_new['TotalPayBenefits'].idxmax()]


# In[87]:


data_new[data_new['TotalPayBenefits'] == data_new['TotalPayBenefits'].max()]  #highest paid salary


# In[86]:


data_new[data_new['TotalPayBenefits'] == data_new['TotalPayBenefits'].min()]['EmployeeName'] #lowest paid salary


# # Summary of Insights

# salaries from 2011 to 2014 is almost in the same range
# 
# 
# 
# GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY	is the job title with the hieghest salary
# 
# 
# 
# Correlation between BasePay and TotalPay is Negative
# 
# 
# Over 4 years BasePay and TotalPay is increase
# 
# 
# 
# there is no strong correlation between BasePay and OvertimePay
# 
# 
# Chief Investment Officer with the lowest salary

# In[ ]:





# In[ ]:




