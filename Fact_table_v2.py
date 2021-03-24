#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


date_ids = {}
special_measures_dimension = pd.read_csv("special_measures.csv")
date_dimension = pd.read_csv("dates.csv")
individual_dimension = pd.read_csv("individual_dimension.csv")
phu_dimension = pd.read_csv("PHU_location_dimension.csv")
weather_dimension = pd.read_csv("weather_dimension.csv")
mobility_dimension = pd.read_csv("mobility_dimension.csv")


# # In[4]:


# individuals = pd.read_csv("conposcovidloc.csv")


# # In[5]:


# individuals.head()


# # In[6]:


# removeCities = individuals[(individuals['Reporting_PHU_City'] != 'Toronto') & (individuals['Reporting_PHU_City'] != 'Ottawa')].index
# individuals.drop(removeCities, inplace=True)
# individuals.head()


# # In[7]:


# individuals['Case_Reported_Date']= pd.to_datetime(individuals['Case_Reported_Date'])
# start_date = pd.to_datetime("1/04/2020")
# end_date = pd.to_datetime("7/31/2020")
# individuals = individuals.loc[(individuals['Case_Reported_Date'] > start_date) & (individuals['Case_Reported_Date'] < end_date)]
# individuals.head()


# # In[8]:


# individuals_outcome = individuals
# individuals_outcome.head()


# # In[9]:


# individuals_outcome = individuals_outcome.drop(['Accurate_Episode_Date', 'Client_Gender', 'Age_Group', 'Test_Reported_Date', 'Specimen_Date', 'Case_AcquisitionInfo', 'Client_Gender', 'Reporting_PHU_ID', 'Reporting_PHU', 'Reporting_PHU_Address', 'Reporting_PHU_Postal_Code', 'Reporting_PHU_Website', 'Reporting_PHU_Latitude', 'Reporting_PHU_Longitude'], axis=1)
# individuals_outcome.head()


# # In[10]:


# individuals_outcome = individuals_outcome.drop(['Case_Reported_Date', 'Outbreak_Related', 'Reporting_PHU_City'], axis=1)
# individuals_outcome.head()


# # In[11]:


# individuals_outcome.rename(columns = {"Row_ID": "Individual_key"}, inplace=True)
# individuals_outcome.head()


# # In[12]:


# individuals_outcome.Outcome1.unique()


# # In[13]:


# individuals_outcome['Resolved'] = 'NaN'
# individuals_outcome['Fatal'] = 'NaN'


# # In[14]:


# individuals_outcome.head()


# # In[15]:


# individuals_outcome.loc[individuals_outcome['Outcome1'] == 'Resolved', 'Resolved'] = "yes"
# individuals_outcome.loc[individuals_outcome['Outcome1'] == 'Resolved', 'Fatal'] = "no"
# individuals_outcome.loc[individuals_outcome['Outcome1'] == 'Fatal', 'Fatal'] = "yes"
# individuals_outcome.loc[individuals_outcome['Outcome1'] == 'Fatal', 'Resolved'] = "no"
# individuals_outcome.head()


# # In[16]:


# individuals_outcome = individuals_outcome.drop(['Outcome1'], axis=1)
# individuals_outcome.head()


# # In[17]:


# def merge_special_measures_with_individual():
#     sms = []
#     sm_ids = []
#     for index, row in special_measures_dimension.iterrows():
#         s_id = row['start_date_id']
#         e_id = row['end_date_id']
#         sms.append((row['StartDate'], row['EndDate'], row['ID'], row['includesOttawa'], row['includesToronto']))

#     for index, row in individual_dimension.iterrows():
#         sm_id = -1
#         for special_measure in sms:
#             if row['date'] >= special_measure[0] and row['date'] <= special_measure[1]:
#                 allow = (row['reporting_phu_city'] == 'Toronto' and special_measure[4] == 'yes') or (row['reporting_phu_city'] == 'Ottawa' and special_measure[3] == 'yes')
#                 if allow:
#                     sm_id = int(special_measure[2])
#                     if sm_id != 3: break
#         sm_ids.append(sm_id)

#     individual_dimension['special_measure_id'] = sm_ids
    
# merge_special_measures_with_individual()


# # In[18]:


# individual_dimension.head()


# # In[19]:


# individual_dimension.rename(columns = {"individual_id": "Individual_key"}, inplace=True)
# individual_dimension.head()


# # In[20]:


# individuals_outcome = individuals_outcome.merge(individual_dimension[["Individual_key","special_measure_id"]], on="Individual_key")
# individuals_outcome.head()


# # In[21]:


# individuals_outcome.rename(columns = {"special_measure_id": "Special_Measure_Key"}, inplace=True)
# individuals_outcome.head()


# # In[22]:


# phu_dimension = phu_dimension.rename(columns={"Reporting_PHU_City": "reporting_phu_city"})
# phu_dimension


# # In[23]:


# fact_table2 = pd.merge(individual_dimension, phu_dimension, how="left", on="reporting_phu_city")
# fact_table2


# # In[24]:


# individuals_outcome = individuals_outcome.merge(fact_table2[["Individual_key","Reporting_PHU_ID"]], on="Individual_key")
# individuals_outcome.head()


# # In[25]:


# weather_dimension.head()


# # In[26]:


# weather_dimension = weather_dimension.rename(columns={"Date/Time": "date"})
# weather_dimension.head()


# # In[27]:


# display(weather_dimension.dtypes) 
# display(fact_table2.dtypes) 
# display(individuals_outcome.dtypes) 


# # In[28]:


# weather_dimension['date'] = pd.to_datetime(weather_dimension['date'])
# display(weather_dimension.dtypes) 


# # In[29]:


# fact_table2 = fact_table2.merge(weather_dimension[["date","weather_id"]], on="date")
# fact_table2.head()


# # In[71]:


# individuals_outcome = individuals_outcome.merge(fact_table2[["Individual_key","weather_id"]], on="Individual_key")
# individuals_outcome.head()


# # In[72]:


# individuals_outcome.rename(columns = {"weather_id": "Weather_Key"}, inplace=True)
# individuals_outcome.head()


# # In[73]:


# roleplaying_dates = pd.read_csv("conposcovidloc.csv")
# roleplaying_dates.head()


# # In[120]:


# # standard data cleaning
# removeCities = roleplaying_dates[(roleplaying_dates['Reporting_PHU_City'] != 'Toronto') & (roleplaying_dates['Reporting_PHU_City'] != 'Ottawa')].index
# roleplaying_dates.drop(removeCities, inplace=True)
# roleplaying_dates['Case_Reported_Date']= pd.to_datetime(roleplaying_dates['Case_Reported_Date'])
# start_date = pd.to_datetime("4/01/2020")
# end_date = pd.to_datetime("7/31/2020")
# roleplaying_dates = roleplaying_dates.loc[(roleplaying_dates['Case_Reported_Date'] > start_date) & (roleplaying_dates['Case_Reported_Date'] < end_date)]
# roleplaying_dates.head()


# # In[77]:


date_dimension = date_dimension.rename(columns={"id": "date_ID"})
build_date = pd.to_datetime(date_dimension.year*10000+date_dimension.month*100+date_dimension.day,format='%Y%m%d')
date_dimension.insert(4, "date_new", build_date, True)
date_dimension.head()


# # In[78]:


# display(date_dimension.dtypes)


# # In[125]:


# # individuals['date_new'].loc[individuals['date_new'] == date_dimension['date_new'].values] = date_dimension['date_ID']

# # individuals.head()

# # data['column2'] = data.apply(lambda x: compare_dates(x.column1, x.column2), axis=1)

# # individuals.head()

# date_dimension['date_new'] = pd.to_datetime(date_dimension['date_new']).dt.date
# roleplaying_dates['Accurate_Episode_Date'] = pd.to_datetime(roleplaying_dates['Accurate_Episode_Date']).dt.date


# # In[134]:


def load_dates():
    dates = pd.read_csv("dates.csv")
    print(dates.head())
    for index, row in date_dimension.iterrows():
        date_ids[row['date_new']] = row['date_ID']
load_dates()
print(date_ids)
        
# def compare_dates(column_name):
#     status = False
#     dt_ids = []
#     for index, row in roleplaying_dates.iterrows():
#         if row[column_name] in date_ids:
#             dt_ids.append(date_ids[row[column_name]])
#         else: 
#             dt_ids.append("NaN")
# #         status = False
# #         for idx, rw in date_dimension.iterrows():
# #             if row[column_name] == rw['date_new']:                
# #                 dt_ids.append(rw['date_ID'])
# #                 status = True
# #         if status == False:
# #             print(column_name)
# #             dt_ids.append("NaN")
    
#     roleplaying_dates[column_name] = dt_ids


# # In[135]:


# roleplaying_dates.head()


# # In[136]:


# compare_dates('Accurate_Episode_Date')
# roleplaying_dates.head()


# # In[137]:


# compare_dates('Case_Reported_Date')
# roleplaying_dates.head()


# # In[138]:


# compare_dates('Test_Reported_Date')
# roleplaying_dates.head()


# # In[139]:


# compare_dates('Specimen_Date')
# roleplaying_dates.head()


# # In[140]:


# roleplaying_dates.rename(columns = {"Accurate_Episode_Date": "onset_date_id"}, inplace=True)
# roleplaying_dates.rename(columns = {"Case_Reported_Date": "reported_date_id"}, inplace=True)
# roleplaying_dates.rename(columns = {"Test_Reported_Date": "test_date_id"}, inplace=True)
# roleplaying_dates.rename(columns = {"Specimen_Date": "specimen_date_id"}, inplace=True)
# roleplaying_dates.head()


# # In[141]:


# roleplaying_dates.rename(columns = {"Row_ID": "Individual_key"}, inplace=True)
# individuals_outcome = individuals_outcome.merge(roleplaying_dates[["Individual_key","onset_date_id"]], on="Individual_key")
# roleplaying_dates.head()


# # In[142]:


# individuals_outcome = individuals_outcome.merge(roleplaying_dates[["Individual_key","reported_date_id"]], on="Individual_key")


# # In[143]:


# individuals_outcome = individuals_outcome.merge(roleplaying_dates[["Individual_key","test_date_id"]], on="Individual_key")


# # In[144]:


# individuals_outcome = individuals_outcome.merge(roleplaying_dates[["Individual_key","specimen_date_id"]], on="Individual_key")


# # In[145]:


# individuals_outcome.head()


# # In[1]:


# individuals_outcome.rename(columns = {"Individual_key": "Individual_Key"}, inplace=True)
# individuals_outcome.rename(columns = {"Reporting_PHU_ID": "PHU_Key"}, inplace=True)
# individuals_outcome.rename(columns = {"onset_date_id": "Onset_Date_Key"}, inplace=True)
# individuals_outcome.rename(columns = {"reported_date_id": "Reported_Date_Key"}, inplace=True)
# individuals_outcome.rename(columns = {"test_date_id": "Test_Date_Key"}, inplace=True)
# individuals_outcome.rename(columns = {"specimen_date_id": "Specimen_Date_Key"}, inplace=True)


# # In[146]:


# individuals_outcome.to_csv("fact_table_v2.csv",index=False)


# # In[ ]:




