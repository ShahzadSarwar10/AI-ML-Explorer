import numpy as np

# create a 2-D array 
array1 = np.array([[2, 4, 6],
                  [1, 3, 5]])
# check the dimension of array1
print(array1.ndim) 
# Output: 2

# Next  run
print (" Next  run")
array1 = np.array([[1, 2, 3],
                 [6, 7, 8]])
# return total number of elements in array1
print(array1.size)
# Output: 6

# Next  run
print (" Next  run")
array1 = np.array([[1, 2, 3],
                [6, 7, 8]])
# return a tuple that gives size of array in each dimension
print(array1.shape)
# Output: (2,3)

# Next  run
print (" Next  run")
# create an array of integers 
array1 = np.array([6, 7, 8])
# check the data type of array1
print(array1.dtype) 
# Output: int64

# Next  run
print (" Next  run")
# create a default 1-D array of integers
array1 = np.array([6, 7, 8, 10, 13])
# create a 1-D array of 32-bit integers 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
# use of itemsize to determine size of each array element of array1 and array2
print(array1.itemsize)  # prints 8
print(array2.itemsize)  # prints 4
#8
#4


# Next  run
print (" Next  run")
array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],
                   	    [6, 7, 8]])
# print memory address of array1's and array2's data
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)
#Data of array1 is: <memory at 0x7f746fea4a00>
#Data of array2 is:  <memory at 0x7f746ff6a5a0>