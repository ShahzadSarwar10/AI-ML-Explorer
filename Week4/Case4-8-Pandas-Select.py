#Pandas Select
#Pandas select refers to the process of extracting specific portions of data from a DataFrame.

import pandas as pd

# create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 22, 27, 29],
    'Salary': [50000, 60000, 45000, 55000, 52000]
}

df = pd.DataFrame(data)

# selecting a single column
name_column = df['Name']

print("Selecting single column: Name")
print(name_column)
print()

# selecting multiple columns
age_salary_columns = df[['Age', 'Salary']]

print("Selecting multiple columns: Age and Salary")
print(age_salary_columns.to_string(index=False))
print()

# selecting rows using slicing
selected_rows = df[1:4]

print("Selecting rows 1 to 3")
print(selected_rows.to_string(index=False))
print()

"""Selecting single column: Name
0      Alice
1        Bob
2    Charlie
3      David
4        Eve
Name: Name, dtype: object

Selecting multiple columns: Age and Salary
Age  Salary
25   50000
30   60000
22   45000
27   55000
29   52000

Selecting rows 1 to 3
Name      Age  Salary
Bob        30    60000
Charlie    22    45000
David      27    55000"""

#Using loc and iloc to Select Data
#The loc and iloc methods in Pandas are used to access data by using label or integer index.
#loc selects rows and columns with specific labels
#iloc selects rows and columns at specific index

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 27, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'San Francisco']
}

df = pd.DataFrame(data)
print(f"Original DataFrame \n {df} \n") 

# loc to select rows and columns by labels
# select rows 1 to 3 and columns Name and Age
selected_data_loc = df.loc[1:3, ['Name', 'Age']]

print(selected_data_loc.to_string(index = False))
print() 

# iloc to select rows and columns by index
# select rows 1 to 3 and columns 0 and 2 
selected_data_iloc = df.iloc[1:4, [0, 2]]

print(selected_data_iloc.to_string(index = False))

"""
Original DataFrame 
       Name  Age           City
0    Alice   25       New York
1      Bob   30    Los Angeles
2  Charlie   22        Chicago
3    David   27        Houston
4    Emily   29  San Francisco 

Name     Age
Bob       30
Charlie   22
David     27

Name        City
Bob      Los Angeles
Charlie  Chicago
David    Houston"""

#Select Rows Based on Specific Criteria

# creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 28, 24],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
}

df = pd.DataFrame(data)

# select rows where Age is greater than 25
selected_rows = df[df['Age'] > 25]

print(selected_rows)

"""     Name  Age Gender
1    Bob   30   Male
3  David   28   Male"""


#query() to Select Data
#The query() method in Pandas allows you to select data using a more SQL-like syntax.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 35],
    'Score': [85, 90, 75, 80, 95]
}

df = pd.DataFrame(data)

# select the rows where the age is greater than 25
selected_rows = df.query('Age > 25')

print(selected_rows.to_string(index = False))

"""
Name  Age  Score
Bob    30     90
David  28     80
Eva    35     95"""


#Select Rows Based on a List of Values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 22, 28, 24]
}

df = pd.DataFrame(data)

# create a list of names to select
names_to_filter = ['Bob', 'David']

# use isin() to select rows based on the 'Name' column
selected_rows = df[df['Name'].isin(names_to_filter)]

print(selected_rows.to_string(index = False))

"""Name  Age
Bob   30
David 28"""


