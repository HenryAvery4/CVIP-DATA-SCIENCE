#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[3]:


dt = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\globalterrorismdb_0718dist.csv",encoding='latin1')
dt.head()


# In[4]:


dt.columns.values


# In[5]:


dt.rename(columns={'iyear':'Year','imonth':'Month','iday':"day",'gname':'Group','country_txt':'Country','region_txt':'Region','provstate':'State','city':'City','latitude':'latitude',
    'longitude':'longitude','summary':'summary','attacktype1_txt':'Attacktype','targtype1_txt':'Targettype','weaptype1_txt':'Weapon','nkill':'kill',
     'nwound':'Wound'},inplace=True)


# In[6]:


dt = dt[['Year','Month','day','Country','State','Region','City','latitude','longitude',"Attacktype",'kill',
               'Wound','target1','summary','Group','Targettype','Weapon','motive']]


# In[7]:


dt.head()


# In[8]:


dt.shape


# In[9]:


dt.isnull().sum()


# In[10]:


dt['Wound'] = dt['Wound'].fillna(0)
dt['kill'] = dt['kill'].fillna(0)


# In[11]:


dt['Casualities'] = dt['kill'] + dt['Wound']


# In[12]:


dt.info()


# In[13]:


dt.describe()


# In[14]:


year = dt['Year'].unique()
years_count = dt['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = year,
           y = years_count,
           palette = "flare")
plt.xticks(rotation = 50)
plt.xlabel('year',fontsize=20)
plt.ylabel('no of attacks every year',fontsize=20)
plt.title('Attacks In Years',fontsize=30)
plt.show()


# In[15]:


pd.crosstab(dt.Year, dt.Region).plot(kind='area',stacked=True,figsize=(20,10))
plt.title('Terrorist Activities By Region',fontsize=25)
plt.ylabel('no of attacks',fontsize=20)
plt.xlabel("year",fontsize=20)
plt.show()


# In[16]:


print("TOP 10 COUNTRIES GETTING ATTACKED")
attack = dt.Country.value_counts()[:10]
attack


# In[17]:


print("TERRORIST GROUPS")
dt.Group.value_counts()[1:10]


# In[31]:


plt.subplots(figsize=(20,10))
sns.barplot(dt['Country'].value_counts()[:10].index,dt['Country'].value_counts()[:10].values,palette='flare')
plt.title('AFFECTED COUNTRIES')
plt.xlabel('COUNTRIES')
plt.ylabel('NUMBER')
plt.xticks(rotation = 50)
plt.show()


# In[34]:


df = dt[['Year','kill']].groupby(['Year']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
df.plot(kind='bar',alpha=0.7,ax=ax4,color="red")
plt.xticks(rotation = 50)
plt.title("DEATH RATE",fontsize=25)
plt.ylabel("No of people dead",fontsize=20)
plt.xlabel('year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(True)
right_side = ax4.spines["right"]
right_side.set_visible(True)


# In[36]:


dt['City'].value_counts().to_frame().sort_values('City',axis=0,ascending=False).head(10).plot(kind='bar',figsize=(20,10),color='green')
plt.xticks(rotation = 50)
plt.xlabel("city",fontsize=15)
plt.ylabel("No of attack",fontsize=15)
plt.title("Top 10 Cities",fontsize=20)
plt.show()


# In[43]:


dt['Attacktype'].value_counts().plot(kind='bar',figsize=(20,10),color='red')
plt.xticks(rotation = 50)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("Number of attack",fontsize=15)
plt.title("ATTACKTYPE",fontsize=20)
plt.show()


# In[42]:


dt[['Attacktype','Wound']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color='black')
plt.xticks(rotation=50)
plt.title("INJURIES",fontsize=20)
plt.ylabel('no of people',fontsize=15)
plt.xlabel('attack type',fontsize=15)
plt.show()


# In[44]:


dt[['Attacktype','kill']].groupby(["Attacktype"],axis=0).sum().plot(kind='bar',figsize=(20,10),color='RED')
plt.xticks(rotation=50)
plt.title("death",fontsize=20)
plt.ylabel('no of people',fontsize=15)
plt.xlabel('attack type',fontsize=15)
plt.show()


# In[37]:


plt.subplots(figsize=(20,10))
sns.countplot(dt["Targettype"],order=dt['Targettype'].value_counts().index,palette="gist_heat",edgecolor=sns.color_palette("flare"));
plt.xticks(rotation=90)
plt.xlabel("Attacktype",fontsize=15)
plt.ylabel("count",fontsize=15)
plt.title("Attack per year",fontsize=20)
plt.show()


# In[ ]:





# In[38]:


dt['Group'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='red',figsize=(20,10))
plt.title("Top 10 terrorist groups",fontsize=20)
plt.xlabel("group name",fontsize=15)
plt.ylabel("no of attacks",fontsize=15)
plt.show()


# In[39]:


dt[['Group','kill']].groupby(['Group'],axis=0).sum().drop('Unknown').sort_values('kill',ascending=False).head(10).plot(kind='bar',color='red',figsize=(20,10))
plt.title("Top 10 terrorist attacks",fontsize=20)
plt.xlabel("terrorist group name",fontsize=15)
plt.ylabel("No of killed people",fontsize=15)
plt.show()


# In[27]:


df=dt[['Group','Country','kill']]
df=df.groupby(['Group','Country'],axis=0).sum().sort_values('kill',ascending=False).drop('Unknown').reset_index().head(10)
df


# In[28]:


kill = dt.loc[:,'kill']
print('No of people killed by attacks:', int(sum(kill.dropna())))


# In[29]:


kills = dt.pivot_table(columns='Attacktype', values='kill', aggfunc='sum')
kills


# In[ ]:





# In[30]:


country_affect = dt.pivot_table(columns='Country', values='kill', aggfunc='sum')
country_affect


# In[ ]:




