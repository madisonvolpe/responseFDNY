#import pandas as pd 
import pandas as pd 
import datetime
import time
#read in data
fdny_df = pd.read_csv('/Users/madisonvolpe/documents/Projects/FDNY_ResponseTimes/RawData/FDNY_Monthly_Response_Times.csv') 

#inspect first five rows
fdny_df.head()

fdny_df.info() #inspecting data types of dataframe

#Now we will filter for those in YEARMONTH with FY distinction
fiscalyear = fdny_df.YEARMONTH.str.contains('^FY')
fdny_df_fil = fdny_df[fiscalyear]

#We will also filter for "All Fire/Emergency Incidents"
emer_inc = fdny_df.INCIDENTCLASSIFICATION.str.contains("All Fire/Emergency Incidents")
fdny_df_fil = fdny_df_fil[emer_inc]

#check the unique valaues of YEARMONTH and INCIDENTCLASSIFICATION columns 
print(fdny_df_fil.YEARMONTH.unique())
print(fdny_df_fil.INCIDENTCLASSIFICATION.unique())

#add hours via strftime 
fdny_df_fil['AVERAGERESPONSETIME']=list(map(lambda x: datetime.datetime.strptime(x,'%M:%S').strftime('%H:%M:%S'),               fdny_df_fil['AVERAGERESPONSETIME']))
fdny_df_fil.AVERAGERESPONSETIME.head()

#convert to time 
fdny_df_fil['AVERAGERESPONSETIME']=list(map(lambda x: time.strptime(x,'%H:%M:%S'),               fdny_df_fil['AVERAGERESPONSETIME']))

#make seconds columns 
fdny_df_fil['SECONDS'] = list(map(lambda x:datetime.timedelta                                  (hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds(),                                 fdny_df_fil['AVERAGERESPONSETIME']))
fdny_df_fil.SECONDS.head()

#this is the average incident count and average response time in seconds from FY 2010 to FY 2017 by borough! 
fdny_df_fil.groupby('INCIDENTBOROUGH').agg({'INCIDENTCOUNT': 'mean', 'SECONDS': 'mean'})

