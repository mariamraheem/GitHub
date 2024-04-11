# Mariam Raheem, Xerac Akhtar

#For the following questions, load the iris.csv dataset into a Pandas
#DataFrame. Make sure you set up an absolute path as described in 
#lecture, and if you're working with others, you should each update
#it to work on your computer.

#import os
import pandas as pd

path = r'/Users/mariamraheem/Documents/GitHub/DAP1/Lab Week 4/iris.csv'

#1. Explore the data.  How many categories of flowers are there? What
#   are the mean and median values, and the standard deviation?  How 
#   would you find the mean values per type of flower?  Right now you
#   can implement this with subsetting; next week we will cover how to
#   do this using groupby.
df_iris = pd.read_csv(path)
df_iris

df_iris.head()
df_iris.tail()
df_iris.shape

df_iris['species'].unique()

df_iris.describe().round(2)
df_iris.describe().loc[['mean','50%','std','max']].round(2)

df_iris

my_species = {'setosa', 'versicolor', 'virginica'}
df_iris.pivot_table(values={'sepal_length','sepal_width','petal_length','petal_width'},
                    index='species',
                    aggfunc={'mean','median','std'}).round(2).T
    

#2. Locate the max value across all four measures.  Use loc to display
#   just the rows that contain those values.
df_iris.iloc[:, :4].describe().loc[['max']]

max_vals = df_iris.idxmax()
max_rows = df_iris.loc[max_vals]
print(max_rows)

#3. How many of observations for each species of iris is in the data?
my_species = {'setosa', 'versicolor', 'virginica'}
for x in my_species:
    print(x, df_iris[df_iris['species'] == x]['species'].count())

#4. Using one line of code FOR EACH COLUMN, divide each value by the mean for that measure,
#   and assign the result to four new columns.  How is this different from 
#   a zscore?  How would you make this a zscore instead?  What's the problem
#   with doing this without accounting for the values in the species column?

def zscore(x):
    return (x - x.mean()) / x.std()

# Normalizing data for each characteristic
my_iris = {'sepal_length','sepal_width','petal_length','petal_width'}

for char in my_iris:
    df_iris[f'{char}_mean'] = df_iris[char] / df_iris[char].mean(axis=0)
    df_iris[f'{char}_zscore'] = zscore(df_iris[char])
    
#5. Create a new column named "petal_area" which is equal to the length
#   times the width.  Note that this isn't really the area of the petal, since
#   petals presumably aren't rectangles.

df_iris['petal_area'] = df_iris['petal_length'] * df_iris['petal_width']

#6. Subset the data to a new variable that is a dataframe with only virginica 
#   flowers.  Now add a new column to this subset that is equal to 1 if the 
#   sepal_length is greater than the mean sepal_length, else 0.  Did you get a
#   SettingWithCopyWarning message?  Modify your copying to do away with the 
#   warning.  Hint: You can create this with apply, or with map if you also
#   create a global variable holding the mean.

# With SettingWithCopyWarning message
df_virginica = df_iris[df_iris['species'] == 'virginica']

mean_sepal_length = df_virginica['sepal_length'].mean()

def above_mean(x):
    return 1 if x > mean_sepal_length else 0

df_virginica['above_mean_sepal_length'] = df_virginica['sepal_length'].apply(above_mean)
df_virginica['above_mean_sepal_length'] = df_virginica['sepal_length'].map(above_mean)

# Method 1: Using .loc to avoid error warning
df_virginica.loc[:,'above_mean_sepal_length'] = df_virginica['sepal_length'].apply(above_mean)

# Method 2: Creating a new object
df_virginica = df_iris[df_iris['species'] == 'virginica'].copy()
df_virginica['above_mean_sepal_length'] = df_virginica['sepal_length'].apply(above_mean)