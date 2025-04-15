"""Python Pandas Filtering
Filtering data is a common operation in data analysis. Pandas allows us to filter data based on different conditions.

We can filter the data in Pandas in two main ways:

By column names (Labels)
By the actual data inside (Values)
"""
#Filter Data By Labels

import pandas as pd

# create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use the filter() method to select columns based on a condition
filtered_df = df.filter(items=['Name', 'Salary']) 

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)

"""Original DataFrame:
      Name Department  Salary
0    Alice         HR   50000
1      Bob  Marketing   60000
2  Charlie  Marketing   55000
3    David         IT   70000


Filtered DataFrame:
      Name  Salary
0    Alice   50000
1      Bob   60000
2  Charlie   55000
3    David   70000"""

#Filter Data By Values
"""We can also filter data by values. Some of the common ways to filter data by values are:

Using logical operator
The isin() method
The str Accessor
The query() method"""

#Logical Operators
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use logical operators to filter
filtered_df = df[df.Salary > 55000]

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)

"""Original DataFrame:
      Name Department  Salary
0    Alice         HR   50000
1      Bob  Marketing   60000
2  Charlie  Marketing   55000
3    David         IT   70000


Filtered DataFrame:
    Name Department  Salary
1    Bob  Marketing   60000
3  David         IT   70000"""

#The isin() Method
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use isin() method
departments = ['HR', 'IT']
filtered_df = df[df.Department.isin(departments)]

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)

"""Original DataFrame:
      Name Department  Salary
0    Alice         HR   50000
1      Bob  Marketing   60000
2  Charlie  Marketing   55000
3    David         IT   70000


Filtered DataFrame:
    Name Department  Salary
0  Alice         HR   50000
3  David         IT   70000"""


#The str Accessor
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use str accessor
filtered_df = df[df.Department.str.contains('Market')]

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)


"""Original DataFrame:
      Name Department  Salary
0    Alice         HR   50000
1      Bob  Marketing   60000
2  Charlie  Marketing   55000
3    David         IT   70000

Filtered DataFrame:
      Name Department  Salary
1      Bob  Marketing   60000
2  Charlie  Marketing   55000"""

#The query() Method
# create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Department': ['HR', 'Marketing', 'Marketing', 'IT'],
        'Salary': [50000, 60000, 55000, 70000]}

df = pd.DataFrame(data)

# display the original DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# use query method
filtered_df = df.query('Salary > 55000 and Department == "Marketing"')

# display the filtered DataFrame
print("Filtered DataFrame:")
print(filtered_df)

"""Original DataFrame:
      Name Department  Salary
0    Alice         HR   50000
1      Bob  Marketing   60000
2  Charlie  Marketing   55000
3    David         IT   70000


Filtered DataFrame:
  Name Department  Salary
1  Bob  Marketing   60000"""
