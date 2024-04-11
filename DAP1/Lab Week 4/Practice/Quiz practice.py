#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:45:51 2024

@author: mariamraheem
"""

import pandas as pd

# Create a dictionary with the data
data = {
    'col1': [10, 20, 30],
    'col2': [111, 222, 333],
    'col3': ['a', 'b', 'c']
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

df.loc[[0, 2], ['col1', 'col3']]
df.iloc[[0, 2], [0, 2]]
df[['col1', 'col3']].iloc[[0, 2]]