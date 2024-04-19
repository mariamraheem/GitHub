# Mariam Raheem, Xerac Akhtar, Anoosha Imran

import pandas as pd

#1. It's a puzzle! Load these three dataframes and explore their structure.
#Then combine them so that the result is a single dataframe with the columns 
#"date", "place", "value1", "value2", with the date columns being datetime 
#objects that run from 1/2020 to 10/2021, without modifying any starter code.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Making date formats consistent
for x in (df1, df2, df3):
    x['date'] = pd.to_datetime(x['date'])

# Rearranging df1
df1.reset_index(inplace=True)
df1_long = pd.wide_to_long(df1, stubnames='place', i='index', j='values').reset_index()
df1_long['date'] = pd.to_datetime(df1_long['date'])
df1_long.drop(columns=['index'], inplace=True)

df1_long.rename(columns={'values': 'place', 'place': 'value1'}, inplace=True)

df1_long.head() 

# Rearranging df2
df2_long = pd.wide_to_long(df2, stubnames='place', i='date', j='place_x').reset_index()
df2_long['date'] = pd.to_datetime(df2_long['date'])
df2_long.rename(columns={'place': 'value2', 'place_x': 'place'}, inplace=True)

df2_long.head()

# Rearranging df3
df3.head() 
df3['place'] = df3['place'].str.replace('place', '')
df3['place'] = df3['place'].astype(int)

# Merge df1, df2, and df3 on 'date' and 'place' columns
df_combined = pd.merge(df1_long, df2_long, on=['date', 'place'], how='outer')
df_combined = pd.merge(df_combined, df3, on=['date', 'place'], how='outer')
df_combined = df_combined.combine_first(df3)

df_combined.sort_values(by=['date', 'place'], inplace=True)

df_combined['value1'] = df_combined['value1_x'].combine_first(df_combined['value1_y'])
df_combined = df_combined.drop(columns=['value1_x', 'value1_y'])
df_combined.reset_index(drop=True, inplace=True)

df_combined.head()
df_combined.shape

print(df_combined)

#2. You had to do some merging in part 1. If you did not already, go back and use
#some assert statements to verify that the dataframes did what you expected.
start_len = len(df1)
end_len = len(df_combined)
assert(start_len == end_len), 'Dataframe expanded after merge'

assert df_combined.shape == (16,4)
assert df_combined['place'].nunique() == len(df_combined), "The 'place' column is not unique."
assert df_combined['date'].nunique() == len(df_combined), "The 'date' column is not unique."

df_combined.drop_duplicates(subset=['place', 'date'], inplace=True)

#3. Is the dataframe from part 1 in long or wide format? Write code to convert it
#into the other.

df_wide = df_combined.pivot(index='date', columns='place')
df_wide