# Mariam Raheem, Xerac Akhtar, Anoosha Imran

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys
group_q1 = df.groupby(['clarity','color'])
group_q1

# 2) Display the describe() output JUST for group color=E, clarity=SI2
group_q2 = df.groupby(['color', 'clarity'])
group_q2.get_group(('E','SI2')).describe().round(2)

# 3) Display the max value for price in each group
group_q2.apply(lambda g: g['price'].max())

# 4) Display the min value for price in each group
group_q2.apply(lambda g: g['price'].min())

# 5) Write four different functions:
#    - one that works with map on the values in a column
#    - one that works with apply on the values in a row
#    - one that works with apply on the values in a column
#    - one that works with apply on a groupby object

# Function 1: Create a dummy for prices > 10,000  
df['price>10000'] = df['price'].map(lambda p: 1 if p > 10000 else 0)
# Function 2: Mean for all rows where color == E
df['cut'].apply(lambda x: x.replace('Ideal', 'Pretty OK I guess'))
# Function 3: Formatting all prices to 2 decimal points 
df['price'].map(lambda x: f'{x:.2f}')
# Function 4: Grouping by color and lisitng max price
df.groupby('color').apply(lambda g: g['price'].max())

# Lab Solutions
def apply_row_func(r):
    r['x'] = (r['x'] + r['y']) * r['z']
    return r
df.apply(apply_row_func,axis=1)

def apply_col_func(c):
    return c - c.mean()
df[['x','y','z']].apply(apply_col_func)

def groupby_func(g):
    g['new_col'] = g['x'] - g['y'].mean()
    return g
df.groupby('cut').apply(groupby_func)

# 6) Display only the maximum price for each clarity.
df.groupby('clarity').apply(lambda g: g['price'].max())
df.groupby('clarity')['price'].max()

# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?
zc = df.groupby('clarity',
                group_keys=False)['carat'].apply(
                    lambda v: (v - v.mean()) /v.std() )
                    
df['zcarat'] = zc
df.groupby('clarity')['zcarat'].max()
