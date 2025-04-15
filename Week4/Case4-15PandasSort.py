#Pandas Sort
#Sorting is a fundamental operation in data manipulation and analysis that involves arranging data in a specific order.

#Sort DataFrame in Pandas

import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [28, 22, 25]}
df = pd.DataFrame(data)
# sort DataFrame by Age in ascending order
sorted_df = df.sort_values(by='Age')
print(sorted_df.to_string(index=False))

"""Name    Age
Bob     22
Charlie 25
Alice   28"""

#Sort Pandas DataFrame by Multiple Columns

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 22, 30, 22],
        'Score': [85, 90, 75, 80]}

df = pd.DataFrame(data)

# 1. Sort DataFrame by 'Age' and then by 'Score' (Both in ascending order)
df1 = df.sort_values(by=['Age', 'Score'])

print("Sorting by 'Age' (ascending) and then by 'Score' (ascending):\n")
print(df1.to_string(index=False))

print()
# 2. Sort DataFrame by 'Age' in ascending order, and then by 'Score' in descending order
df2 = df.sort_values(by=['Age', 'Score'], ascending=[True, False])

print("Sorting by 'Age' (ascending) and then by 'Score' (descending):\n")
print(df2.to_string(index=False))

"""Name    Age  Score
Bob     22    90
David   22    80
Alice   25    85
Charlie 30    75"""

#Sort Pandas Series
ages = pd.Series([28, 22, 25], name='Age')

# sort Series in ascending order
sorted_ages = ages.sort_values()

print(sorted_ages.to_string(index=False))

"""22
25
28"""


##index Sort Pandas DataFrame Using sort_index()

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [28, 22, 25]}
# create a DataFrame with a non-sequential index
df = pd.DataFrame(data, index=[2, 0, 1])

print("Original DataFrame:")
print(df.to_string(index=True))
print("\n")

# sort DataFrame by index in ascending order
sorted_df = df.sort_index()

print("Sorted DataFrame by index:")
print(sorted_df.to_string(index=True))

"""Original DataFrame:
     Name    Age
2    Alice   28
0    Bob     22
1    Charlie 25

Sorted DataFrame by index:
    Name    Age
0   Bob     22
1   Charlie 25
2   Alice   28"""
