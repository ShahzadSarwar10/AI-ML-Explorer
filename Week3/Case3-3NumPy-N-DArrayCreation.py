import numpy as np

# create a 2D array with 2 rows and 4 columns
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(array1)
#[[1 2 3 4]
# [5 6 7 8]]

# create a 3D array with 2 "slices", each of 3 rows and 4 columns
array1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8], 
                [9, 10, 11, 12]],
                     
                [[13, 14, 15, 16], 
                 [17, 18, 19, 20], 
                 [21, 22, 23, 24]]])

print(array1)

"""
[[[ 1  2  3  4]
  [ 5  6  7  8]
  [ 9 10 11 12]]

 [[13 14 15 16]
  [17 18 19 20]
  [21 22 23 24]]]  """


# Next  run
print (" Next  run")
# create 2D array with 2 rows and 3 columns filled with zeros
array1 = np.zeros((2, 3))
print("2-D Array: ")
print(array1)
# create 3D array with dimensions 2x3x4 filled with zeros
array2 = np.zeros((2, 3, 4))
print("\n3-D Array: ")
print(array2)

"""2-D Array: 
[[0. 0. 0.]
 [0. 0. 0.]]

3-D Array: 
[[[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]

 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]]"""

# Next  run
print (" Next  run")
# Create a 2-D array with elements initialized to 5 
numpy_array = np.full((2, 2), 5)
print("Array:", numpy_array)

#[[5 5]
#[5 5]]


# Next  run
print (" Next  run")
# create a 2D array of 2 rows and 2 columns of random numbers
array1 = np.random.rand(2, 2)
print("2-D Array: ")
print(array1)
# create a 3D array of shape (2, 2, 2) of random numbers
array2 = np.random.rand(2, 2, 2)
print("\n3-D Array: ")
print(array2)

"""2-D Array: 
[[0.13198621 0.54730421]
 [0.36570987 0.16233836]]

3-D Array: 
[[[0.15666007 0.4580507 ]
  [0.84769856 0.76699589]]

 [[0.45395202 0.39944328]
  [0.62999479 0.39629496]]]"""


# Next  run
print (" Next  run")
# create an empty 2D array with 2 rows and 2 columns
array1 = np.empty((2, 2))
print("2-D Array: ")
print(array1)
# create an empty 3D array of shape (2, 2, 2) 
array2 = np.empty((2, 2, 2))
print("\n3-D Array: ")
print(array2)


"""2-D Array: 
[[8.86495615e-317 0.00000000e+000]
 [2.21149159e-316 1.76125651e-312]]

3-D Array: 
[[[1.0749539e-316 0.0000000e+000]
  [0.0000000e+000 0.0000000e+000]]

 [[0.0000000e+000 0.0000000e+000]
  [0.0000000e+000 0.0000000e+000]]]"""

