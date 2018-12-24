
# coding: utf-8

# In[4]:


#import pandas as pd 
import pandas as pd 
import datetime
import time
#read in data
fdny_df = pd.read_csv('/Users/madisonvolpe/documents/Projects/FDNY_ResponseTimes/RawData/FDNY_Monthly_Response_Times.csv') 


# In[17]:


#inspect first five rows
fdny_df.head()


# In[18]:


fdny_df.info() #inspecting data types of dataframe


# In[19]:


#Now we will filter for those in YEARMONTH with FY distinction
fiscalyear = fdny_df.YEARMONTH.str.contains('^FY')
fdny_df_fil = fdny_df[fiscalyear]

#We will also filter for "All Fire/Emergency Incidents"
emer_inc = fdny_df.INCIDENTCLASSIFICATION.str.contains("All Fire/Emergency Incidents")
fdny_df_fil = fdny_df_fil[emer_inc]


# In[20]:


#check the unique valaues of YEARMONTH and INCIDENTCLASSIFICATION columns 
print(fdny_df_fil.YEARMONTH.unique())
print(fdny_df_fil.INCIDENTCLASSIFICATION.unique())


# In[21]:


#add hours via strftime 
fdny_df_fil['AVERAGERESPONSETIME']=list(map(lambda x: datetime.datetime.strptime(x,'%M:%S').strftime('%H:%M:%S'),               fdny_df_fil['AVERAGERESPONSETIME']))


# In[22]:


fdny_df_fil.AVERAGERESPONSETIME.head()


# In[23]:


#convert to time 
fdny_df_fil['AVERAGERESPONSETIME']=list(map(lambda x: time.strptime(x,'%H:%M:%S'),               fdny_df_fil['AVERAGERESPONSETIME']))


# In[27]:


#make seconds columns 
fdny_df_fil['SECONDS'] = list(map(lambda x:datetime.timedelta                                  (hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds(),                                 fdny_df_fil['AVERAGERESPONSETIME']))


# In[28]:


fdny_df_fil.SECONDS.head()


# In[29]:


#this is the average incident count and average response time in seconds from FY 2010 to FY 2017 by borough! 
fdny_df_fil.groupby('INCIDENTBOROUGH').agg({'INCIDENTCOUNT': 'mean', 'SECONDS': 'mean'})

