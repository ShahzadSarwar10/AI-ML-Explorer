import numpy as np

# create a list named list1
list1 = [2, 4, 6, 8]

# create numpy array using list1
array1 = np.array(list1)

print(array1)

# Output: [2 4 6 8]

# Next  run
print (" Next  run")
#Instead of creating a list and using the list variable with the np.array() function, we can directly pass list elements as an argument. For example,
# create numpy array using a list
array1 = np.array([2, 4, 6, 8])
print(array1)

# Output: [2  4  6 8]


# Next  run
print (" Next  run")
#The np.zeros() function allows us to create an array filled with all zeros. For example,
# create an array with 4 elements filled with zeros
array1 = np.zeros(4)
print(array1)
# Output: [0. 0. 0. 0.]


# Next  run
print (" Next  run")
#The np.arange() function returns an array with values within a specified interval. For example,
# create an array with values from 0 to 4
array1 = np.arange(5)
print("Using np.arange(5):", array1)
# create an array with values from 1 to 8 with a step of 2
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):",array2)
#Using np.arange(5): [0 1 2 3 4]
#Using np.arange(1, 9, 2): [1 3 5 7]

# Next  run
print (" Next  run")
# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)
#[0.08455648 0.56379034 0.66463204 0.97608605 0.30700052]

# Next  run
print (" Next  run")
# create an empty array of length 4
array1 = np.empty(4)
print(array1)
#[1.47966080e-316 0.00000000e+000 9.06092203e-312 2.47218893e-253]
