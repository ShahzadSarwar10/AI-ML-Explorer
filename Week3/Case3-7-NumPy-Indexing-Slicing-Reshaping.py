import numpy as np

array1 = np.array([1, 3, 5, 7, 9])

# access numpy elements using index
print(array1[0])    # prints 1
print(array1[2])    # prints 5
print(array1[4])    # prints 9


# create a numpy array
numbers = np.array([2, 4, 6, 8, 10])
# change the value of the first element
numbers[0] = 12
print("After modifying first element:",numbers)    # prints [12 4 6 8 10]
# change the value of the third element
numbers[2] = 14
print("After modifying third element:",numbers)    # prints [12 4 14 8 10]

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([1, 3, 5, 7, 9])
# access the last element
print(numbers[-1])    # prints 9
# access the second-to-last element
print(numbers[-2])    # prints 7

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 3, 5, 7, 11])
# modify the last element
numbers[-1] = 13
print(numbers)    # Output: [2 3 5 7 13]
# modify the second-to-last element
numbers[-2] = 17
print(numbers)    # Output: [2 3 5 17 13]


# Next  run
print (" Next  run")
# create a 2D array 
array1 = np.array([[1, 3, 5, 7], 
                       [9, 11, 13, 15],
                       [2, 4, 6, 8]])
# access the element at the second row and fourth column
element1 = array1[1, 3]  # returns 15
print("4th Element at 2nd Row:",element1)  
# access the element at the first row and second column
element2 = array1[0, 1]  # returns 3
print("2nd Element at First Row:",element2)

# Next  run
print (" Next  run")
# create a 2D array 
array1 = np.array([[1, 3, 5], 
             [7, 9, 2], 
             [4, 6, 8]])
# access the second row of the array
second_row = array1[1, :]
print("Second Row:", second_row)  # Output: [7 9 2]
# access the third column of the array
third_col = array1[:, 2]
print("Third Column:", third_col)  # Output: [5 2 8]


# Next  run
print (" Next  run")
# create a 3D array with shape (2, 3, 4)
array1 = np.array([[[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]],
                     
                    [[13, 14, 15, 16], 
                    [17, 18, 19, 20], 
                    [21, 22, 23, 24]]])
# access a specific element of the array
element = array1[1, 2, 1]
# print the value of the element
print(element) 
# Output: 22


# Next  run
print (" Next  run")
# create a 1D array 
array1 = np.array([1, 3, 5, 7, 8, 9, 2, 4, 6])
# slice array1 from index 2 to index 6 (exclusive)
print(array1[2:6])  # [5 7 8 9]
# slice array1 from index 0 to index 8 (exclusive) with a step size of 2
print(array1[0:8:2])  # [1 5 8 2]
# slice array1 from index 3 up to the last element
print(array1[3:])  # [7 8 9 2 4 6]
# items from start to end
print(array1[:])   # [1 3 5 7 8 9 2 4 6]

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify elements from index 3 onwards
numbers[3:] = 20
print(numbers)
# Output: [ 2  4  6 20 20 20]


# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify the first 3 elements
numbers[:3] = 40
print(numbers)
# Output: [40 40 40  8 10 12]


# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify the first 3 elements
numbers[:3] = 40
print(numbers)
# Output: [40 40 40  8 10 12]

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# modify every second element from indices 1 to 5
numbers[1:5:2] = 16
print(numbers)
# Output: [ 2 16  6 16 10 12]

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# slice the last 3 elements of the array
# using the start parameter
print(numbers[-3:])    # [8 10 12]
# slice elements from 2nd-to-last to 4th-to-last element
# using the start and stop parameters
print(numbers[-5:-2])    # [4 6 8] 
# slice every other element of the array from the end
# using the start, stop, and step parameters
print(numbers[-1::-2])   # [12 8 4]

# Next  run
print (" Next  run")
# create a numpy array
numbers = np.array([2, 4, 6, 8, 10, 12])
# generate reversed array
reversed_numbers = numbers[::-1]
print(reversed_numbers)
# Output: [12 10 8 6 4 2]

# Next  run
print (" Next  run")
# create a 2D array
array1 = np.array([[1, 3, 5, 7], 
                   [9, 11, 13, 15]])
print(array1[:2, :2])
# Output
"""[[ 1  3]
 [ 9 11]]"""


# Next  run
print (" Next  run")
# create a 2D array
array1 = np.array([[1, 3, 5, 7], 
                   [9, 11, 13, 15]])
print(array1[:2, :2])
# Output
#[[ 1  3]
# [ 9 11]]

# Next  run
print (" Next  run")
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
# reshape a 1D array into a 2D array 
# with 2 rows and 4 columns
result = np.reshape(array1, (2, 4))
print(result)

"""[[1 3 5 7]
[2 4 6 8]]"""

# Next  run
print (" Next  run")
# reshape a 1D array into a 2D array 
# with 4 rows and 2 columns
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
result1 = np.reshape(array1, (4, 2))
print("With 4 rows and 2 columns: \n",result1)
# reshape a 1D array into a 2D array with a single row
result2 = np.reshape(array1, (1, 8))
print("\nWith a single row: \n",result2)

"""With 4 rows and 2 columns: 
[[1 3]
 [5 7]
 [2 4]
 [6 8]]

With a single row: 
 [[1 3 5 7 2 4 6 8]]"""

# Next  run
print (" Next  run")
# create a 1D array
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])
# reshape the 1D array to a 3D array
result = np.reshape(array1, (2, 2, 2))
# print the new array
print("1D to 3D Array: \n",result)

"""1D to 3D Array: 
[[[1 3]
  [5 7]]

 [[2 4]
  [6 8]]]"""

# Next  run
print (" Next  run")
# flatten 2D array to 1D
array1 = np.array([[1, 3], [5, 7], [9, 11]])
result1 = np.reshape(array1, -1)
print("Flattened 2D array:", result1)
# flatten 3D array to 1D
array2 = np.array([[[1, 3], [5, 7]], [[2, 4], [6, 8]]])
result2 = np.reshape(array2, -1)
print("Flattened 3D array:", result2)

"""Flattened 2D array: [ 1  3  5  7  9 11]
Flattened 3D array: [1 3 5 7 2 4 6 8]"""


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(array1):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(array1):
    print(index, elem)