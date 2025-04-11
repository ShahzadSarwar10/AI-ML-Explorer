import numpy as np

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])
# using the + operator
result1 = first_array + second_array
print("Using the + operator:",result1) 
# using the add() function
result2 = np.add(first_array, second_array)
print("Using the add() function:",result2) 
"""Using the + operator: [ 3  7 11 15]
Using the add() function: [ 3  7 11 15]"""

# Next  run
print (" Next  run")
first_array = np.array([3, 9, 27, 81])
second_array = np.array([2, 4, 8, 16])
# using the - operator
result1 = first_array - second_array
print("Using the - operator:",result1) 
# using the subtract() function
result2 = np.subtract(first_array, second_array)
print("Using the subtract() function:",result2) 
"""Using the - operator: [ 1  5 19 65]
Using the subtract() function: [ 1  5 19 65]"""

# Next  run
print (" Next  run")
first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])
# using the * operator
result1 = first_array * second_array
print("Using the * operator:",result1) 
# using the multiply() function
result2 = np.multiply(first_array, second_array)
print("Using the multiply() function:",result2) 
"""Using the * operator: [ 2 12 30 56]
Using the multiply() function: [ 2 12 30 56]"""

# Next  run
print (" Next  run")
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
# using the / operator
result1 = first_array / second_array
print("Using the / operator:",result1) 
# using the divide() function
result2 = np.divide(first_array, second_array)
print("Using the divide() function:",result2) 
"""Using the / operator: [0.25 0.4  0.5 ]
Using the divide() function: [0.25 0.4  0.5 ]"""

# Next  run
print (" Next  run")
array1 = np.array([1, 2, 3])
# using the ** operator
result1 = array1 ** 2
print("Using the ** operator:",result1) 
# using the power() function
result2 = np.power(array1, 2)
print("Using the power() function:",result2) 
"""Using the ** operator: [1 4 9]
Using the power() function: [1 4 9]"""

# Next  run
print (" Next  run")
first_array = np.array([9, 10, 20])
second_array = np.array([2, 5, 7])
# using the % operator
result1 = first_array % second_array
print("Using the % operator:",result1) 
# using the mod() function
result2 = np.mod(first_array, second_array)
print("Using the mod() function:",result2)
"""Using the % operator: [1 0 6]
Using the mod() function: [1 0 6]"""

# Next  run
print (" Next  run")
# create a 1D array
array1 = np.array([1, 3, 5, 7, 9, 11])
# reshape the 1D array into a 2D array
array2 = np.reshape(array1, (2, 3))
# transpose the 2D array
array3 = np.transpose(array2)
print("Original array:\n", array1)
print("\nReshaped array:\n", array2)
print("\nTransposed array:\n", array3)
"""Original array:
[ 1  3  5  7  9 11]

Reshaped array:
 [[ 1  3  5]
 [ 7  9 11]]

Transposed array:
 [[ 1  7]
 [ 3  9]
 [ 5 11]]"""


# Next  run
print (" Next  run")
# create two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 9, 16, 25, 36])
# add the two arrays element-wise
arr_sum = np.add(array1, array2)
# subtract the array2 from array1 element-wise
arr_diff = np.subtract(array1, array2)
# compute square root of array2 element-wise
arr_sqrt = np.sqrt(array2)
print("\nSum of arrays:\n", arr_sum)
print("\nDifference of arrays:\n", arr_diff)
print("\nSquare root of first array:\n", arr_sqrt)

"""Sum of arrays:
[ 5 11 19 29 41]

Difference of arrays:
 [ -3  -7 -13 -21 -31]

Square root of first array:
 [2. 3. 4. 5. 6.]"""

# Next  run
print (" Next  run")
# create a numpy array
marks = np.array([76, 78, 81, 66, 85])
# compute the mean of marks
mean_marks = np.mean(marks)
print("Mean:",mean_marks)
# compute the median of marks
median_marks = np.median(marks)
print("Median:",median_marks)
# find the minimum and maximum marks
min_marks = np.min(marks)
print("Minimum marks:", min_marks)
max_marks = np.max(marks)
print("Maximum marks:", max_marks)



# Next  run
print (" Next  run")
array1 = np.array([1, 2, 3])
array2 = np.array([3, 2, 1])
# less than operator
result1 = array1 < array2
print("array1 < array2:",result1)    # Output: [ True False False]
# greater than operator
result2 = array1 > array2
print("array1 > array2:",result2)    # Output: [False False  True]
# equal to operator
result3 = array1 == array2
print("array1 == array2:",result3)    # Output: [False  True False]
"""array1 < array2: [ True False False]
array1 > array2: [False False  True]
array1 == array2: [False  True False]"""


# Next  run
print (" Next  run")
array1 = np.array([9, 12, 21])
array2 = np.array([21, 12, 9])
# use of less()
result = np.less(array1, array2)
print("Using less():",result)    # Output: [ True False False]
# use of less_equal()
result = np.less_equal(array1, array2)
print("Using less_equal():",result)     # Output: [ True  True False]
# use of greater()
result = np.greater(array1, array2)
print("Using greater():",result)    # Output: [False False  True]
# use of greater_equal()
result = np.greater_equal(array1, array2)
print("Using greater_equal():",result)    # Output: [False  True  True]
# use of equal()
result = np.equal(array1, array2)
print("Using equal():",result)    # Output: [False  True False]
# use of not_equal()
result = np.not_equal(array1, array2)
print("Using not_equal():",result)    # Output: [ True False  True]
"""Using less(): [ True False False]
Using less_equal(): [ True  True False]
Using greater(): [False False  True]
Using greater_equal(): [False  True  True]
Using equal(): [False  True False]
Using not_equal(): [ True False  True]"""


# Next  run
print (" Next  run")
x1 = np.array([True, False, True])
x2 = np.array([False, False, True])
# Logical AND
print(np.logical_and(x1, x2)) # Output: [False False  True]
# Logical OR
print(np.logical_or(x1, x2)) # Output: [ True False  True]
# Logical NOT
print(np.logical_not(x1)) # Output: [False  True False]

# Next  run
print (" Next  run")
# array of angles in radians
angles = np.array([0, 1, 2])
print("Angles:", angles)
# compute the sine of the angles
sine_values = np.sin(angles)
print("Sine values:", sine_values)
# compute the inverse sine of the angles
inverse_sine = np.arcsin(angles)
print("Inverse Sine values:", inverse_sine)
"""Angles: [0 1 2]
Sine values: [0.         0.84147098 0.90929743]
Inverse Sine values: [0.         1.57079633        nan]"""

# Next  run
print (" Next  run")
# define an angle in radians
angle =  1.57079633
print("Initial angle in radian:", angle)
# convert the angle to degrees
angle_degree = np.degrees(angle)
print("Angle in degrees:", angle_degree)
# convert the angle back to radians
angle_radian = np.radians(angle_degree)
print("Angle in radians (after conversion):", angle_radian)
"""Initial angle in radian: 1.57079633
Angle in degrees: 90.0000001836389
Angle in radians (after conversion): 1.57079633"""

# Next  run
print (" Next  run")
numbers = np.array([1.23456, 2.34567, 3.45678, 4.56789])
# round the array to two decimal places
rounded_array = np.round(numbers, 2)
print(rounded_array)
# Output: [1.23 2.35 3.46 4.57]

# Next  run
print (" Next  run")
array1 = np.array([1.23456, 2.34567, 3.45678, 4.56789])
print("Array after floor():", np.floor(array1))
print("Array after ceil():", np.ceil(array1))
"""Array after floor(): [1. 2. 3. 4.]
Array after ceil(): [2. 3. 4. 5.]"""

# Next  run
print (" Next  run")
# create a 1D array with 5 elements
array1 = np.array([1, 2, 3, 4, 5])                                                                                                    
# calculate the median
median = np.median(array1)
print(median) 
# Output: 3.0

# Next  run
print (" Next  run")
# create a 1D array with 6 elements
array1 = np.array([1, 2, 3, 4, 5, 7])
# calculate the median
median = np.median(array1)
print(median) 
# Output: 3.5


# Next  run
print (" Next  run")
# create a 2D array
array1 = np.array([[2, 4, 6], 
                   [8, 10, 12], 
                   [14, 16, 18]])
# compute median along horizontal axis 
result1 = np.median(array1, axis=1)
print("Median along horizontal axis :", result1)
# compute median along vertical axis
result2 = np.median(array1, axis=0)
print("Median along vertical axis:", result2)
# compute median of entire array
result3 = np.median(array1)
print("Median of entire array:", result3)
"""Median along horizontal axis : [ 4. 10. 16.]
Median along vertical axis: [ 8. 10. 12.]
Median of entire array: 10.0"""

# Next  run
print (" Next  run")
# create a numpy array
marks = np.array([76, 78, 81, 66, 85])
# compute the mean of marks
mean_marks = np.mean(marks)
print(mean_marks)
# Output: 77.2

# Next  run
print (" Next  run")
# create a 2D array
array1 = np.array([[1, 3], 
                 [5, 7]])
# calculate the mean of the entire array
result1 = np.mean(array1)
print("Entire Array:",result1)  # 4.0
# calculate the mean along vertical axis (axis=0)
result2 = np.mean(array1, axis=0)
print("Along Vertical Axis:",result2)  # [3. 5.]
# calculate the mean along  (axis=1)
result3 = np.mean(array1, axis=1)
print("Along Horizontal Axis :",result3)  # [2. 6.]
"""Entire Array: 4.0
Along Vertical Axis: [3. 5.]
Along Horizontal Axis : [2. 6.]"""

# Next  run
print (" Next  run")
# create a numpy array
marks = np.array([76, 78, 81, 66, 85])
# compute the standard deviation of marks
std_marks = np.std(marks)
print(std_marks)
# Output: 6.803568381206575


# Next  run
print (" Next  run")
# create a 2D array
array1 = np.array([[2, 5, 9], 
                 [3, 8, 11], 
                 [4, 6, 7]])
# compute standard deviation along horizontal axis
result1 = np.std(array1, axis=1)
print("Standard deviation along horizontal axis:", result1)
# compute standard deviation along vertical axis
result2 = np.std(array1, axis=0)
print("Standard deviation  along vertical axis:", result2)
# compute standard deviation of entire array
result3 = np.std(array1)
print("Standard deviation of entire array:", result3)
"""Standard deviation along horizontal axis: [2.86744176 3.29983165 1.24721913]
Standard deviation along vertical axis: [0.81649658 1.24721913 1.63299316]
Standard deviation of entire array: 2.7666443551086073"""


# Next  run
print (" Next  run")
# create an array
array1 = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
# compute the 25th percentile of the array
result1 = np.percentile(array1, 25)
print("25th percentile:",result1)
# compute the 75th percentile of the array
result2 = np.percentile(array1, 75)
print("75th percentile:",result2)
"""25th percentile: 5.5
75th percentile: 14.5"""

# Next  run
print (" Next  run")
# create an array
array1 = np.array([2,6,9,15,17,22,65,1,62])
# find the minimum value of the array
min_val = np.min(array1)
# find the maximum value of the array
max_val = np.max(array1)
# print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)

"""Minimum value: 1
Maximum value: 65"""

# Next  run
print (" Next  run")
##Example: NumPy Broadcasting
# create 1-D array
array1 = np.array([1, 2, 3])
# create 2-D array
array2 = np.array([[1], [2], [3]])
# add arrays of different dimension
# size of array1 expands to match with array2
sum = array1 + array2
print(sum)
"""[[2 3 4]
 [3 4 5]
 [4 5 6]]"""

# Next  run
print (" Next  run")
#Broadcasting with Scalars
# 1-D array
array1 = np.array([1, 2, 3])
# scalar
number = 5
# add scalar and 1-D array
sum = array1 + number
print(sum)
#[6 7 8]

# Next  run
print (" Next  run")
#Select Multiple Elements Using NumPy Fancy Indexing
# create a numpy array
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8]) 
# select elements at index 1, 2, 5, 7
select_elements = array1[[1, 2, 5, 7]]
print(select_elements)
# Output: [2 3 6 8]

# Next  run
print (" Next  run")
#Example: NumPy Fancy Indexing
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# select a single element
simple_indexing = array1[3]
print("Simple Indexing:",simple_indexing)   # 4
# select multiple elements
fancy_indexing = array1[[1, 2, 5, 7]]
print("Fancy Indexing:",fancy_indexing)   # [2 3 6 8]
"""Simple Indexing: 4
Fancy Indexing: [2 3 6 8]"""

# Next  run
print (" Next  run")
#Fancy Indexing for Sorting NumPy Array
array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])
# sort array1 using fancy indexing
sorted_array = array1[np.argsort(array1)]
print(sorted_array)
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Next  run
print (" Next  run")
#We could also use fancy indexing to sort the array in descending order.
array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])
# sort array1 using fancy indexing in descending order
sorted_array = array1[np.argsort(-array1)]
print(sorted_array)
# Output: [8 7 6 5 4 3 2 1]

# Next  run
print (" Next  run")
#Fancy Indexing to Assign New Values to Specific Elements
array1 = np.array([3, 2, 6, 1, 8, 5, 7, 4])
# create a list of indices to assign new values
indices = [1, 3, 6]
# create a new array of values to assign
new_values = [10, 20, 30]
# use fancy indexing to assign new values to specific elements
array1[indices] = new_values
print(array1)
# Output: [ 3 10  6 20  8  5 30  4]

# Next  run
print (" Next  run")
#Fancy Indexing on N-d Arrays
# create a 2D array
array1 = np.array([[1, 3, 5], 
                [11, 7, 9], 
                [13, 18, 29]])
# create an array of row indices
row_indices = np.array([0, 2])
# use fancy indexing to select specific rows
selected_rows = array1[row_indices, :]
print(selected_rows)
"""[[ 1  3  5]
 [13 18 29]]"""


#Perform Matrix Multiplication in NumPy
# create two matrices
matrix1 = np.array([[1, 3], 
             		[5, 7]])             
matrix2 = np.array([[2, 6], 
                    [4, 8]])
# calculate the dot product of the two matrices
result = np.dot(matrix1, matrix2)
print("matrix1 x matrix2: \n",result)
"""matrix1 x matrix2: 
[[14 30]
 [38 86]]"""

#Transpose NumPy Matrix
""""Matrix:
a11    a12    
a21    a22    

Transposed Matrix:
a11    a21
a12    a22"""
# create a matrix
matrix1 = np.array([[1, 3], 
             		[5, 7]])
# get transpose of matrix1
result = np.transpose(matrix1)
print(result)
"""[[1 5]
 [3 7]]"""

#Calculate Inverse of a Matrix in NumPy
# create a 3x3 square matrix
matrix1 = np.array([[1, 3, 5], 
             		[7, 9, 2],
                    [4, 6, 8]])
# find inverse of matrix1
result = np.linalg.inv(matrix1)
print(result)
"""[[-1.11111111 -0.11111111  0.72222222]
 [ 0.88888889  0.22222222 -0.61111111]
 [-0.11111111 -0.11111111  0.22222222]]"""

#Find Determinant of a Matrix in NumPy
#We can find the determinant of a square matrix using the np.linalg.det() function to calculate the determinant of the given matrix.
# create a matrix
matrix1 = np.array([[1, 2, 3], 
             		[4, 5, 1],
                    [2, 3, 4]])
# find determinant of matrix1
result = np.linalg.det(matrix1)
print(result)
#-5.00


#Flatten Matrix in NumPy
#Flattening a matrix simply means converting a matrix into a 1D array.
# create a 2x3 matrix
matrix1 = np.array([[1, 2, 3], 
             		[4, 5, 7]])
result = matrix1.flatten()
print("Flattened 2x3 matrix:", result)
#Flattened 2x3 matrix: [1 2 3 4 5 7]

