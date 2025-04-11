import numpy as np

# create an array of integers 
array1 = np.array([2, 4, 6])
# check the data type of array1
print(array1.dtype) 
# Output: int64

# Next  run
print (" Next  run")
# create an array of  integers
int_array = np.array([-3, -1, 0, 1])
# create an array of floating-point numbers
float_array = np.array([0.1, 0.2, 0.3])
# create an array of complex numbers
complex_array = np.array([1+2j, 2+3j, 3+4j])
# check the data type of int_array
print(int_array.dtype)  # prints int64
# check the data type of float_array
print(float_array.dtype)  # prints float64
# check the data type of complex_array
print(complex_array.dtype)  # prints complex128

"""int64
float64
complex128"""

# Next  run
print (" Next  run")
# create an array of 32-bit integers
array1 = np.array([1, 3, 7], dtype='int32')
print(array1, array1.dtype)
#[1 3 7] int32

# Next  run
print (" Next  run")
# create an array of 8-bit integers
array1 = np.array([1, 3, 7], dtype='int8')
# create an array of unsigned 16-bit integers
array2 = np.array([2, 4, 6], dtype='uint16')
# create an array of 32-bit floating-point numbers
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
# create an array of 64-bit complex numbers
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
# print the arrays and their data types
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)

"""[1 3 7] int8
[2 4 6] uint16
[1.2 2.3 3.4] float32
[1.+2.j 2.+3.j 3.+4.j] complex64"""


# Next  run
print (" Next  run")
# create an array of integers
int_array = np.array([1, 3, 5, 7])
# convert data type of int_array to float
float_array = int_array.astype('float')
# print the arrays and their data types
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)

#[1 3 5 7] int64
#[1. 3. 5. 7.] float64

