#Dataframe Operations and Manipulations
#Pandas DataFrame objects come with a variety of built-in functions like head(), tail() and info() that allow us to view and analyze DataFrames.

import pandas as pd

# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}
df = pd.DataFrame(data)

# display the first three rows
print('First Three Rows:')
print(df.head(3))
print()

# display the first five rows
print('First Five Rows:')
print(df.head())


"""First Three Rows:
    Name   Age      City
0   John   25  New York
1  Alice   30     Paris
2    Bob   35    London

First Five Rows:
    Name   Age      City
0   John   25  New York
1  Alice   30     Paris
2    Bob   35    London
3   Emma   28    Sydney
4   Mike   32     Tokyo"""

# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}

df = pd.DataFrame(data)

# display the last three rows
print('Last Three Rows:')
print(df.tail(3))
print()

# display the last five rows
print('Last Five Rows:')
print(df.tail())

"""Last Three Rows:
    Name   Age     City
7  Linda   33   Madrid
8    Tom   29  Toronto
9  Emily   31   Moscow

Last Five Rows:
    Name   Age     City
5  Sarah   27   Berlin
6  David   40     Rome
7  Linda   33   Madrid
8    Tom   29  Toronto
9  Emily   31   Moscow"""


# create dataframe
data = {'Name': ['John', 'Alice', 'Bob', 'Emma', 'Mike', 'Sarah', 'David', 'Linda', 'Tom', 'Emily'],
        'Age': [25, 30, 35, 28, 32, 27, 40, 33, 29, 31],
        'City': ['New York', 'Paris', 'London', 'Sydney', 'Tokyo', 'Berlin', 'Rome', 'Madrid', 'Toronto', 'Moscow']}
df = pd.DataFrame(data)

# get info about dataframe
df.info()
"""<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    10 non-null     object
 1   Age     10 non-null     int64 
 2   City    10 non-null     object
dtypes: int64(1), object(2)
memory usage: 372.0+ bytes"""

""" the info() method provides the following information about a Pandas DataFrame:

Class: The class of the object, which indicates that it is a pandas DataFrame
RangeIndex: The index range of the DataFrame, showing the starting and ending index values
Data columns: The total number of columns in the DataFrame
Column names: The names of the columns in the DataFrame
Non-Null Count: The count of non-null values for each column
Dtype: The data types of the columns
Memory usage: The memory usage of the DataFrame in bytes"""