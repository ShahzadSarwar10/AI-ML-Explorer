""""Pandas DataFrame Manipulation
DataFrame manipulation in Pandas involves editing and modifying existing DataFrames. Some common DataFrame manipulation operations are:

Adding rows/columns
Removing rows/columns
Renaming rows/columns"""


import pandas as pd

#Add a New Column to a Pandas DataFrame
# define a dictionary containing student data
data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
        'Height': [5.5, 6.0, 5.8, 5.3],
        'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']}

# convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# declare a new list
address = ['New York', 'London', 'Sydney', 'Toronto']

# assign the list as a column
df['Address'] = address

print(df)

"""      Name  Height Qualification   Address
0     John     5.5           BSc  New York
1     Emma     6.0           BBA    London
2  Michael     5.8           MBA    Sydney
3   Sophia     5.3           BSc   Toronto"""


#Add a New Row to a Pandas DataFrame
# define a dictionary containing student data
data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
        'Height': [5.5, 6.0, 5.8, 5.3],
        'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']}

# convert the dictionary into a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print()
# add a new row
df.loc[len(df.index)] = ['Amy', 5.2, 'BIT'] 
print("Modified DataFrame:")
print(df)


"""Original DataFrame:
      Name  Height Qualification
0     John    5.5           BSc
1     Emma    6.0           BBA
2  Michael    5.8           MBA
3   Sophia    5.3           BSc

Modified DataFrame:
      Name  Height Qualification
0     John    5.5           BSc
1     Emma    6.0           BBA
2  Michael    5.8           MBA
3   Sophia    5.3           BSc
4      Amy    5.2           BIT"""


#Remove Rows/Columns from a Pandas DataFrame
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Felipe', 'Rita'],
        'Age': [25, 30, 35, 40, 22, 29],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Bogota', 'Banglore']}
df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# delete row with index 4
df.drop(4, axis=0, inplace=True)

# delete row with index 5
df.drop(index=5, inplace=True)

# delete rows with index 1 and 3
df.drop([1, 3], axis=0, inplace=True)

# display the modified DataFrame after deleting rows
print("Modified DataFrame:")
print(df)

""""Original DataFrame:
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
3    David   40     Tokyo

Modified DataFrame:
      Name  Age      City
0    Alice   25  New York
2  Charlie   35     Paris"""

#Example: Delete columns
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo'],
        'Height': ['165', '178', '185', '171'],
        'Profession': ['Engineer', 'Entrepreneur', 'Unemployed', 'Actor'],
        'Marital Status': ['Single', 'Married', 'Divorced', 'Engaged']}
df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# delete age column
df.drop('Age', axis=1, inplace=True)

# delete marital status column
df.drop(columns='Marital Status', inplace=True)

# delete height and profession columns
df.drop(['Height', 'Profession'], axis=1, inplace=True)

# display the modified DataFrame after deleting rows
print("Modified DataFrame:")
print(df)

"""# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo'],
        'Height': ['165', '178', '185', '171'],
        'Profession': ['Engineer', 'Entrepreneur', 'Unemployed', 'Actor'],
        'Marital Status': ['Single', 'Married', 'Divorced', 'Engaged']}
df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# delete age column
df.drop('Age', axis=1, inplace=True)

# delete marital status column
df.drop(columns='Marital Status', inplace=True)

# delete height and profession columns
df.drop(['Height', 'Profession'], axis=1, inplace=True)

# display the modified DataFrame after deleting rows
print("Modified DataFrame:")
print(df)"""

#Rename Labels in a DataFrame

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# rename column 'Name' to 'First_Name'
df.rename(columns= {'Name': 'First_Name'}, inplace=True)

# rename columns 'Age' and 'City'
df.rename(mapper= {'Age': 'Number', 'City':'Address'}, axis=1, inplace=True)

# display the DataFrame after renaming column
print("Modified DataFrame:")
print(df)

""""Original DataFrame:
      Name  Age      City
0    Alice  25  New York
1      Bob  30    London
2  Charlie  35     Paris
3    David  40     Tokyo

Modified DataFrame:
  First_Name  Number   Address
0      Alice     25  New York
1        Bob     30    London
2    Charlie     35     Paris
3      David     40     Tokyo"""


#Example: Rename Row Labels
import pandas as pd

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'London', 'Paris', 'Tokyo']}
df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print()

# rename column one index label
df.rename(index={0: 7}, inplace=True)

# rename columns multiple index labels
df.rename(mapper={1: 10, 2: 100}, axis=0, inplace=True)

# display the DataFrame after renaming column
print("Modified DataFrame:")
print(df)

"""Original DataFrame:
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
3    David   40     Tokyo

Modified DataFrame:
        Name  Age      City
7      Alice   25  New York
10       Bob   30    London
100  Charlie   35     Paris
3      David   40     Tokyo"""


