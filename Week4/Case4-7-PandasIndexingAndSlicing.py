#Pandas Indexing and Slicing
#In Pandas, indexing refers to accessing rows and columns of data from a DataFrame, whereas slicing refers to accessing a range of rows and columns.

import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# access the Name column
names = df['Name']

print(names)
"""0      Alice
1        Bob
2    Charlie
3      David
4        Eve
Name: Name, dtype: object"""



# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# access multiple columns
name_city = df[['Name','City']]

print(name_city)

"""   Name      City
0    Alice  New York
1      Bob     Paris
2  Charlie    London 
3    David     Tokyo
4      Eve    Sydney"""

#Example: Indexing Using .loc
import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# access a single row
single_row = df.loc[2]

print("Single row:")
print(single_row)
print()

# access rows 0, 3 and 4
row_list = df.loc[[0, 3, 4]]

print("List of Rows:")
print(row_list)
print()

# access a list of columns
column_list = df.loc[:,['Name', 'Age']]

print("List of Columns:")
print(column_list)
print()

# access second row of 'Name' column
specific_value = df.loc[1, 'Name']

print("Specific Value:")
print(specific_value)

"""Single row:
Name    Charlie
Age          18
City     London
Name: 2, dtype: object

List of Rows:
    Name  Age      City
0  Alice   25  New York
3  David   47     Tokyo
4    Eve   33    Sydney

List of Columns:
      Name  Age
0    Alice   25
1      Bob   32
2  Charlie   18
3    David   47
4      Eve   33

Specific Value:
Bob"""


#Example: Slicing Using .loc

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}

df = pd.DataFrame(data)

# slice rows from index 1 to 3
slice_rows = df.loc[1:3]

print("Sliced Rows:")
print(slice_rows)
print()

 # slicing columns from 'Name' to 'Age'
slice_columns = df.loc[:, 'Name':'Age']

print("Sliced Columns:")
print(slice_columns)

"""Sliced Rows:
      Name  Age    City
1      Bob   32   Paris
2  Charlie   18  London
3    David   47   Tokyo

Sliced Columns:
      Name  Age
0    Alice   25
1      Bob   32
2  Charlie   18
3    David   47
4      Eve   33"""

#Example: Boolean Indexing With .loc
# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# boolean indexing with .loc
boolean_index = df.loc[df['Age'] > 30]

print("Filtered DataFrame: ")
print(boolean_index)

"""Boolean Indexing:
      Name  Age    City
1      Bob   32   Paris
3    David   47   Tokyo
4      Eve   33  Sydney"""


#Pandas .iloc
#In Pandas, the .iloc property is used to access and modify data within a DataFrame using integer-based indexing. It allows us to select specific rows and columns based on their integer locations.

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# access single row
single_row = df.iloc[2]

# access rows 0, 3 and 4
row_list = df.iloc[[0, 3, 4]]

# access columns 0 and 2
column_list = df.iloc[:,[0,2]]

# access a specific value
specific_value = df.iloc[1, 0]

# display result
print("Single Row:")
print(single_row)
print()
print("List of Rows:")
print(row_list)
print()
print("List of Columns:")
print(column_list)
print()
print("Specific Value:")
print(specific_value)


""""Single Row:
Name    Charlie
Age          18
City     London
Name: 2, dtype: object

List of Rows:
    Name  Age      City
0  Alice   25  New York
3  David   47     Tokyo
4    Eve   33    Sydney

List of Columns:
      Name      City
0    Alice  New York
1      Bob     Paris
2  Charlie    London
3    David     Tokyo
4      Eve    Sydney

Specific Value:
Bob"""


#Example: Slicing Using .iloc
import pandas as pd

# create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 32, 18, 47, 33],
    'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']
}
df = pd.DataFrame(data)

# slice rows from position 1 to 3
slice_rows = df.iloc[1:4]

# slice columns from position 0 to 1
slice_columns = df.iloc[:, 0:2]

# display results
print("Sliced Rows:")
print(slice_rows)
print()
print("Sliced Columns:")
print(slice_columns)

"""Sliced Rows:
      Name  Age    City
1      Bob   32   Paris
2  Charlie   18  London
3    David   47   Tokyo

Sliced Columns:
      Name  Age
0    Alice   25
1      Bob   32
2  Charlie   18
3    David   47
4      Eve   33"""

"""".loc vs .iloc
The main differences between .loc and .iloc are as follows:

Basis	            .loc	                        .iloc
Indexing	        Label-based indexing	        Integer-based indexing
Endpoint	        Endpoint is included	        Endpoint is not included
Boolean indexing	Boolean indexing is supported	Boolean indexing is not supported"""

