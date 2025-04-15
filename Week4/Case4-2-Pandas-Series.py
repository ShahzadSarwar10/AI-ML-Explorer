import pandas as pd
#Pandas Series
#A Pandas Series is a one-dimensional labeled array-like object that can hold data of any type
#A Pandas Series can be thought of as a column in a spreadsheet or a single column of a DataFrame. It consists of two main components: the labels and the data.
"""0    'John'
1    30
2    6.2
3    False
dtype: object"""


# create a list
data = [10, 20, 30, 40, 50]
# create a series from the list
my_series = pd.Series(data)
print(my_series)



# create a list
data = [10, 20, 30, 40, 50]
# create a series from the list
my_series = pd.Series(data)
# display third value in the series
print(my_series[2])
#30


# create a list
a = [1, 3, 5]
# create a series and specify labels
my_series = pd.Series(a, index = ["x", "y", "z"])
print(my_series)

"""x    1
y    3
z    5
dtype: int64"""


# create a list
a = [1, 3, 5]
# create a series and specify labels
my_series = pd.Series(a, index = ["x", "y", "z"])
# display the value with label y
print(my_series["y"])
#3


# create a dictionary
grades = {"Semester1": 3.25, "Semester2": 3.28, "Semester3": 3.75}
# create a series from the dictionary
my_series = pd.Series(grades)
# display the series
print(my_series)
"""Semester1    3.25
Semester2    3.28
Semester3    3.75
dtype: float64"""


# create a dictionary
grades = {"Semester1": 3.25, "Semester2": 3.28, "Semester3": 3.75}
# select specific dictionary items using index argument
my_series = pd.Series(grades, index = ["Semester1", "Semester2"])
# display the series
print(my_series)
"""Semester1    3.25
Semester2    3.28
dtype: float64"""

