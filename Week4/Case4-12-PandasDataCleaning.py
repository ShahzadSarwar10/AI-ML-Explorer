""""Pandas Data Cleaning
Data cleaning means fixing and organizing messy data. Pandas offers a wide range of tools and functions to help us clean and preprocess our data effectively.

Data cleaning often involves:

Dropping irrelevant columns.
Renaming column names to meaningful names.
Making data values consistent.
Replacing or filling in missing values.
"""

#Drop Rows With Missing Values
# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],  
    'B': [None, 2, 3, 4, 5],  
    'C': [1, 2, None, None, 5]
}
df = pd.DataFrame(data)
print("Original Data:\n",df)
print()
# use dropna() to remove rows with any missing values
df_cleaned = df.dropna()
print("Cleaned Data:\n",df_cleaned)

"""Original Data:
     A    B    C
0  1.0  NaN  1.0
1  2.0  2.0  2.0
2  3.0  3.0  NaN
3  NaN  4.0  NaN
4  5.0  5.0  5.0

Cleaned Data:
    A    B    C
1  2.0  2.0  2.0
4  5.0  5.0  5.0"""

#Fill Missing Values
import pandas as pd

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],  
    'B': [None, 2, 3, 4, 5],  
    'C': [1, 2, None, None, 5]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# filling NaN values with 0
df.fillna(0, inplace=True)

print("\nData after filling NaN with 0:\n", df)

"""Original Data:
    A    B    C
0  1.0  NaN  1.0
1  2.0  2.0  2.0
2  3.0  3.0  NaN
3  NaN  4.0  NaN
4  5.0  5.0  5.0
Data after filling NaN with 0:
   A    B    C
0  1.0  0.0  1.0
1  2.0  2.0  2.0
2  3.0  3.0  0.0
3  0.0  4.0  0.0
4  5.0  5.0  5.0"""

#Use Aggregate Functions to Fill Missing Values

# define a dictionary with sample data which includes some missing values
data = {
    'A': [1, 2, 3, None, 5],  
    'B': [None, 2, 3, 4, 5],  
    'C': [1, 2, None, None, 5]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# filling NaN values with the mean of each column
df.fillna(df.mean(), inplace=True)

print("\nData after filling NaN with mean:\n", df)

"""Original Data:
    A    B    C
0  1.0  NaN  1.0
1  2.0  2.0  2.0
2  3.0  3.0  NaN
3  NaN  4.0  NaN
4  5.0  5.0  5.0
Data after filling NaN with mean:
     A    B         C
0  1.00  3.5  1.000000
1  2.00  2.0  2.000000
2  3.00  3.0  2.666667
3  2.75  4.0  2.666667
4  5.00  5.0  5.000000"""

"""Handle Duplicates Values
In Pandas, to handle duplicate rows, we can use the duplicated() and the drop_duplicates() function.

duplicated() - to check for duplicates
drop_duplicates() - remove duplicate rows"""

# sample data
data = {
    'A': [1, 2, 2, 3, 3, 4],
    'B': [5, 6, 6, 7, 8, 8]
}
df = pd.DataFrame(data)

print("Original DataFrame:\n", df.to_string(index=False))

# detect duplicates
print("\nDuplicate Rows:\n", df[df.duplicated()].to_string(index=False))

# remove duplicates based on column 'A'
df.drop_duplicates(subset=['A'], keep='first', inplace=True)

print("\nDataFrame after removing duplicates based on column 'A':\n", df.to_string(index=False))

"""Original DataFrame:
 A  B
 1  5
 2  6
 2  6
 3  7
 3  8
 4  8
Duplicate Rows:
 A  B
 2  6
DataFrame after removing duplicates based on column 'A':
 A  B
 1  5
 2  6
 3  7
 4  8"""

#Rename Column Names to Meaningful Names

# sample data
data = {
    'A': [25, 30, 35],
    'B': ['John', 'Doe', 'Smith'],
    'C': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# rename columns
df.rename(columns={'A': 'Age', 'B': 'Name', 'C': 'Salary'}, inplace=True)

print(df.to_string(index=False))

"""Age  Name  Salary
  25  John   50000
  30   Doe   60000
  35 Smith   70000"""

"""Pandas Handling Wrong Format
In a real world scenario, data are taken from various sources which causes inconsistencies in format of the data. For example, a column can have data of integer and string type as the data is copied from different sources."""

# create dataframe
data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
}
df = pd.DataFrame(data)

# calculate the mean temperature
mean_temperature = df['Temperature'].mean()

print(mean_temperature)

#TypeError: unsupported operand type(s) for +: 'float' and 'str'

#Convert Data to Correct Format
# create dataframe
data = {
    'Country': ['USA', 'Canada', 'Australia', 'Germany', 'Japan'],
    'Date': ['2023-07-20', '2023-07-21', '2023-07-22', '2023-07-23', '2023-07-24'],
    'Temperature': [25.5, '28.0', 30.2, 22.8, 26.3]
}
df = pd.DataFrame(data)

# convert temperature column to float
df['Temperature'] = df['Temperature'].astype(float)

# calculate the mean temperature
mean_temperature = df['Temperature'].mean()

print(mean_temperature)

#26.560000000000002


#Handling Mixed Date Formats
import pandas as pd

# create a sample dataframe with mixed date formats
df = pd.DataFrame({'date': ['2022-12-01', '01/02/2022', '2022-03-23', '03/02/2022', '3 4 2023', '2023.9.30']})

# convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

print(df)

"""
   date
0 2022-12-01
1 2022-02-01
2 2022-03-23
3 2022-02-03
4 2023-04-03
5 2023-09-30"""

"""Pandas Handling Wrong Data
Sometimes, a dataset can have inaccurate entries due to reasons such as human errors during data input, sourcing data from unreliable places, etc.
"""
"""Replace Individual Values
We can see that the value F for Gender column is an obvious mistake. Let's replace F with M to rectify the error."""

import pandas as pd

# create dataframe
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 80, 100],
    'Gender': ['M', 'M', 'M', 'F', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)

# replace F with M
df.loc[3, 'Gender'] = 'M'

print(df)

"""    Name  Age Gender  Standard
0     John    8      M         3
1  Michael    9      M         4
2      Tom    7      M        12
3     Alex   80      M         3
4     Ryan  100      M         5"""

#Replace Values Based on a Condition
#In cases where the values need to satisfy a particular condition, we can iterate through the values to check if the condition is satisfied and to make changes accordingly.

# create dataframe
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 80, 100],
    'Gender': ['M', 'M', 'M', 'M', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)

# replace values based on conditions
for i  in df.index:
    age_val = df.loc[i, 'Age']
    if (age_val > 14) and (age_val%10 == 0):
        df.loc[i, 'Age'] = age_val/10

print(df)

"""   Name  Age Gender  Standard
0     John    8      M         3
1  Michael    9      M         4
2      Tom    7      M        12
3     Alex    8      M         3
4     Ryan   10      M         5"""


"""Remove Wrong Values
Some values can't be corrected. For example, the value 12 in Standard doesn't make any sense as this is an elementary school. But we can't also correct it because we don't know the right standard."""

# create dataframe
data = {
    'Name': ['John', 'Michael', 'Tom', 'Alex', 'Ryan'],
    'Age': [8, 9, 7, 8, 10],
    'Gender': ['M', 'M', 'M', 'M', 'M'],
    'Standard': [3, 4, 12, 3, 5]
}
df = pd.DataFrame(data)

# remove mistaken values
for i in df.index:
    if df.loc[i,'Standard'] > 8:
        df.drop(i, inplace=True)

print(df)

"""  Name  Age Gender  Standard
0     John    8      M         3
1  Michael    9      M         4
3     Alex    8      M         3
4     Ryan   10      M         5"""

