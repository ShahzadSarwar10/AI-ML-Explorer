#Pandas Array
#An array allows us to store a collection of multiple values in a single data structure.
#Pandas array is designed to provide a more memory-efficient and performance-enhanced alternative to Python's built-in lists, NumPy arrays, and other data structures for handling the same type of data.

import pandas as pd

# create a list named data
data = [2, 4, 6, 8]
# create Pandas array using data
array1 = pd.array(data)
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# create Pandas array by passing list directly
array1 = pd.array([2, 4, 6, 8])
print(array1)
"""<IntegerArray>
[2, 4, 6, 8]
Length: 4, dtype: Int64"""


# creating a pandas.array of integers
int_array = pd.array([1, 2, 3, 4, 5], dtype='int')
print(int_array)
print()

# creating a pandas.array of floating-point numbers
float_array = pd.array([1.1, 2.2, 3.3, 4.4, 5.5], dtype='float')
print(float_array)
print()

# creating a pandas.array of strings
string_array = pd.array(['apple', 'banana', 'cherry', 'date'], dtype='str')
print(string_array)
print()

# creating a pandas.array of boolean values
bool_array = pd.array([True, False, True, False], dtype='bool')
print(bool_array)
print()

"""<NumpyExtensionArray>
[1, 2, 3, 4, 5]
Length: 5, dtype: int64

<NumpyExtensionArray>
[1.1, 2.2, 3.3, 4.4, 5.5]
Length: 5, dtype: float64

<NumpyExtensionArray>
['apple', 'banana', 'cherry', 'date']
Length: 4, dtype: str192

<NumpyExtensionArray>
[True, False, True, False]
Length: 4, dtype: bool"""


# create a Pandas array
arr = pd.array([18, 20, 19, 21, 22])
# create a Pandas series from the Pandas array
arr_series = pd.Series(arr)
print(arr_series)
"""0    18
1    20
2    19
3    21
4    22
dtype: Int64"""
