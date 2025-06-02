import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\ankit\OneDrive\Desktop\New folder\classroom\olympics.csv')
# data = data.reset_index(drop=True)
# data = data.drop('Event_gender', axis=1)
# data = data.drop('Country_Code', axis=1)
# data.head()
# print(data)
# print(data.isnull().sum())
# data = data.dropna()
# print(data.isnull().sum())
# data = data.astype({'Year':'int'})
# data.head()

# 1st question/ which city hosted maximum number of olympics
# data = data[['City', 'Year']]
# data = data.drop_duplicates('Year')

# 2nd question/ which city hosted most events.
# data = data['City'].value_counts()
# data.plot.bar(x = 'City', y='Count')
# plt.xlabel('City')
# plt.ylabel('Count')
# plt.show()


# 3rd question/understand the events themselves.
# data = data[['Sport', 'Discipline','Event']].drop_duplicates()
# data = data['Sport'].value_counts()
# plt.figure(figsize=(10,6))
# data.plot.bar(x='Sport',y='Count')
# plt.xlabel('Sport')
# plt.ylabel('Count')
# plt.show()



# 4th / which athlete has win most from given period
# data = data.groupby(['Athlete'])['Athlete'].count().reset_index(name='Count').sort_values(ascending=False,by=['Count'])
# data = data[:10]
# data.plot.bar(x='Athlete',y='Count')
# plt.show()



# 5th / put some light on gender ratio in winning teams?
# data = data.groupby(['Gender'])['Gender'].count()
# plt.figure(figsize=(12,2))
# data.plot.barh(x='Athlete',y='Count')
# plt.show()
# data = data[['Event','Gender']]
# data = data.groupby(['Event','Gender'])['Gender'].count()
# print(data)



# 6th / which country has win most medal and how many in each year?
# data = data[['Year', 'Country', 'Medal']]
# data = data.groupby(['Year', 'Country','Medal'])['Country'].count().reset_index(name = 'Count')
# data['Medal'] = pd.Categorical(data['Medal'],categories=['Gold', 'Silver', 'Bronze'], ordered=True)
# data = data.sort_values(ascending = [True, True, True],by = ['Year', 'Country','Medal'])
# data = data.pivot( index = ['Year','Country'], columns =['Medal'], values = ['Count']).reset_index()
# data = data.replace(np.nan, 0)
# data['Sum'] = data['Count', 'Bronze'] + data['Count','Gold'] + data['Count','Silver']
# data = data.sort_values(ascending = [True, False],by =['Year','Sum'])
# data.columns = data.columns.droplevel(0)
# data.columns = ['Year', 'Country', 'Gold', 'Silver','Bronze', 'Sum']
# print(data.Country.unique())


# 7th / Can you tell me which country has dominated any particular sport?
# data = data.groupby(['Sport','Country'])['Country'].count().reset_index(name ='Count').sort_values(ascending = [True, False],by = ['Sport','Count'])
# print(data.Sport.unique())
# inp = 'Archery'
# try:
#     inp = input("Select a Sport from above list:")
# except:
#     print("Input is interrupted")
# temp = data[data['Sport'] == inp].head(3)
# print(temp)




# 8th / has any athlete changed his or her event or discipline or sport and still win the medal?
# temp = data[['Athlete','Sport']].drop_duplicates()
# temp = temp.groupby(['Athlete'])
# for k,v in temp:
#     if len(v['Sport'].tolist()) >1:
#         print(k,v['Sport'].tolist())
