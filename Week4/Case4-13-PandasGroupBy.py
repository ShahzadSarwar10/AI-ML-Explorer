#Pandas groupby
#In Pandas, the groupby operation lets us group data based on specific columns. This means we can divide a DataFrame into smaller groups based on the values in these columns.

import pandas as pd

# create a dictionary containing the data
data = {'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing'],
        'Sales': [1000, 500, 800, 300]}

# create a DataFrame using the data dictionary
df = pd.DataFrame(data)

# group the DataFrame by the Category column and
# calculate the sum of Sales for each category
grouped = df.groupby('Category')['Sales'].sum()

# print the grouped data
print(grouped)

"""Category
Clothing        800
Electronics    1800
Name: Sales, dtype: int64"""

"""Group by a Multiple Column in Pandas
We can also group multiple columns and calculate multiple aggregates in Pandas."""

# create a DataFrame with student data
data = {
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Grade': ['A', 'B', 'A', 'A', 'B'],
    'Score': [90, 85, 92, 88, 78]
}

df = pd.DataFrame(data)

# define the aggregate functions to be applied to the Score column
agg_functions = {
    # calculate both mean and maximum of the Score column
    'Score': ['mean', 'max'] 
}

# group the DataFrame by Gender and Grade, then apply the aggregate functions
grouped = df.groupby(['Gender', 'Grade']).aggregate(agg_functions)

# print the resulting grouped DataFrame
print(grouped)

"""             Score    
              mean max
Gender Grade          
Female A      88.0  88
       B      85.0  85
Male   A      91.0  92
       B      78.0  78"""

"""Group With Categorical Data
We group with categorical data where we want to analyze data based on specific categories."""

# sample data
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 50, 300, 120]}

df = pd.DataFrame(data)

# convert Category column to categorical type
df['Category'] = pd.Categorical(df['Category'])

# group by Category  and calculate the total sales
grouped = df.groupby('Category')['Sales'].sum()

print(grouped)

"""Category
A    600
B    320
Name: Sales, dtype: int64"""

