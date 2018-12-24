
# coding: utf-8

# In[112]:


#import pandas as pd 
import pandas as pd 

#read in data
fdny_df = pd.read_csv('/Users/madisonvolpe/documents/Projects/FDNY_ResponseTimes/FDNY_Monthly_Response_Times.csv') 


# In[113]:


#inspect first five rows
fdny_df.head()


# In[114]:


fdny_df.info() #inspecting data types of dataframe


# In[115]:


#Now we will filter for those in YEARMONTH with FY distinction
fiscalyear = fdny_df.YEARMONTH.str.contains('^FY')
fdny_df_fil = fdny_df[fiscalyear]

#We will also filter for "All Fire/Emergency Incidents"
emer_inc = fdny_df.INCIDENTCLASSIFICATION.str.contains("All Fire/Emergency Incidents")
fdny_df_fil = fdny_df_fil[emer_inc]


# In[116]:


#check the unique valaues of YEARMONTH and INCIDENTCLASSIFICATION columns 
print(fdny_df_fil.YEARMONTH.unique())
print(fdny_df_fil.INCIDENTCLASSIFICATION.unique())


# In[133]:


#convert AVERAGERESPONSETIME to time 
fdny_df_fil['AVERAGERESPONSETIME']=pd.to_datetime(fdny_df_fil['AVERAGERESPONSETIME'], format='%M:%S')
fdny_df_fil


# In[138]:


fdny_df_fil.groupby('INCIDENTBOROUGH').agg({'INCIDENTCOUNT': 'mean'})

