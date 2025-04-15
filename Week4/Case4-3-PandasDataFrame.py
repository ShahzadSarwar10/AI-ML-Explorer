#Pandas DataFrame
#A DataFrame is like a table where the data is organized in rows and columns. It is a two-dimensional data structure like a two-dimensional array. For example,
"""     Country      Capital      Population
0    Canada       Ottawa       37742154
1    Australia    Canberra     25499884
2    UK           London       67886011
3    Brazil       Brasília     212559417"""
#Country, Capital and Population are the column names.
#Each row represents a record, with the index value on the left. The index values are auto-assigned starting from 0.

import pandas as pd


# create a dictionary
data = {'Name': ['John', 'Alice', 'Bob'],
       'Age': [25, 30, 35],
       'City': ['New York', 'London', 'Paris']}
# create a dataframe from the dictionary
df = pd.DataFrame(data)
print(df)

"""   Name  Age      City
0  John   25  New York
1  Alice  30  London
2  Bob    35  Paris"""


# create a two-dimensional list
data = [['John', 25, 'New York'],
       ['Alice', 30, 'London'],
       ['Bob', 35, 'Paris']]
# create a DataFrame from the list
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)
"""   Name  Age      City
0  John   25  New York
1  Alice  30  London
2  Bob    35  Paris"""


# load data from a CSV file
df = pd.read_csv('data.csv')
print(df)

#We can also create a DataFrame using other file types like JSON, Excel spreadsheet, SQL database, etc. The methods to read different file types are listed below:
#JSON - read_json()
#Excel spreadsheet - read_excel()
#SQL - read_sql()
#

#We can set an existing column as the index using the set_index() method. For example,
# create dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# set the 'Name' column as index
df.set_index('Name', inplace=True)
print(df)
"""Name     Age    City      
John     25  New York
Alice    28    London
Bob      32     Paris"""


#We can create a range index with specific start and end values using the RangeIndex() function. For example,
# create dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# create a range index
df = pd.DataFrame(data, index=pd.RangeIndex(5, 8, name='Index'))
print(df)

""""         Name  Age      City
Index                       
5        John   25  New York
6       Alice   28    London
7         Bob   32     Paris"""

#Renaming Index
# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# display original dataframe
print('Original DataFrame:')
print(df)
print()
# rename index
df.rename(index={0: 'A', 1: 'B', 2: 'C'}, inplace=True)
# display dataframe after index is renamed
print('Modified DataFrame')
print(df)

""""Original DataFrame:
    Name  Age      City
0   John   25  New York
1  Alice   28    London
2    Bob   32     Paris

Modified DataFrame
    Name  Age      City
A   John   25  New York
B  Alice   28    London
C    Bob   32     Paris"""


#Resetting Index
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
# create a dataframe
df = pd.DataFrame(data)
# rename index
df.rename(index={0: 'A', 1: 'B', 2: 'C'}, inplace=True)
# display dataframe
print('Original DataFrame:')
print(df)
print('\n')
# reset index
df.reset_index(inplace=True)
# display dataframe after index is reset
print('Modified DataFrame:')
print(df)
"""Original DataFrame:
    Name  Age      City
A   John   25  New York
B  Alice   28    London
C    Bob   32     Paris

Modified DataFrame:
  index   Name  Age      City
0     A   John   25  New York
1     B  Alice   28    London
2     C    Bob   32     Paris"""


#Access Rows by Index
# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
second_row = df.iloc[1]
print(second_row)

"""Name     Alice
Age         28
City    London
Name: 1, dtype: object"""

#Get DataFrame Index
# create a dataframe
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 28, 32],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# return index object
print(df.index)
# return index values
print(df.index.values)

"""RangeIndex(start=0, stop=3, step=1)
[0 1 2]"""

