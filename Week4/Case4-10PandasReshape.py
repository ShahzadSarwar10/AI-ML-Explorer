#Pandas Reshape
#In Pandas, reshaping data refers to the process of converting a DataFrame from one format to another for better data visualization and analysis.
#Pandas provides multiple methods like pivot(), pivot_table(), stack(), unstack() and melt() to reshape data. We can choose the method based on our analysis requirement.

#Reshape Data Using pivot()

import pandas as pd

# create a DataFrame
data = {'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
        'Category': ['A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40]}
df = pd.DataFrame(data)

print("Original Dataframe:\n", df)

# pivot the  DataFrame
pivot_df = df.pivot(index='Date', columns='Category', values='Value')
print("Reshaped DataFrame:\n", pivot_df)
"""Original Dataframe: 
         Date      Category  Value
0  2023-08-01        A     10
1  2023-08-01        B     20
2  2023-08-02        A     30
3  2023-08-02        B     40

Reshaped DataFrame: 
Category     A   B
Date              
2023-08-01  10  20
2023-08-02  30  40"""

#Reshape Data Using pivot_table()

# create a DataFrame
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Value': [10, 20, 30, 40, 50, 60]}
df = pd.DataFrame(data)
print("Original Dataframe:\n", df)

# create a pivot table
pivot_table_df = df.pivot_table(index='Category', values='Value', aggfunc='mean')
print("Reshaped Dataframe:\n", pivot_table_df)

"""Original Dataframe: 
   Category  Value
0        A     10
1        B     20
2        A     30
3        B     40
4        A     50
5        B     60 

Reshaped Dataframe: 
Value
Category       
A          30.0
B          40.0"""

#Reshape Data Using stack() and unstack()
#In Pandas, we can also use the stack() and unstack() to reshape data.
#stack() is used to pivot a level of the column labels, transforming them into innermost row index levels.
#unstack() is used to pivot a level of the row index, transforming it into an outermost column level

# create a DataFrame
data = {'Date': ['2023-08-01', '2023-08-02'],
        'Category_A': [10, 20],
        'Category_B': [30, 40]}
df = pd.DataFrame(data)

# set 'Date' column as the index
df.set_index('Date', inplace=True)

# stack the columns into rows
stacked_df = df.stack()
print("Stack:\n", stacked_df)
print()

# unstack the rows back to columns
unstacked_df = stacked_df.unstack()
print("Unstack: \n", unstacked_df)


"""Stack:
Date                  
2023-08-01  Category_A    10
            Category_B    30
2023-08-02  Category_A    20
            Category_B    40
dtype: int64

Unstack: 
Category_A  Category_B
Date                              
2023-08-01          10          30
2023-08-02          20          40"""

#Use of melt() to Reshape DataFrame
#The melt() function in Pandas transforms a DataFrame from a wide format to a long format.

# create a sample DataFrame
data = {'Name': ['Alice', 'Bob'],
        'Math': [90, 85],
        'History': [75, 92]}
df = pd.DataFrame(data)

# melt the DataFrame
melted_df = pd.melt(df, id_vars='Name', var_name='Subject', value_name='Score')

print(melted_df)

"""     Name  Subject  Score
0  Alice     Math     90
1    Bob     Math     85
2  Alice  History     75
3    Bob  History     92"""


