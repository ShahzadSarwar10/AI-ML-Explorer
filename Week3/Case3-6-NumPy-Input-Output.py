import numpy as np

# create a NumPy array
array1 = np.array([[1, 3, 5], 
                   [7, 9, 11]])
# save the array to a file
np.save('file1.npy', array1)

# Next  run
print (" Next  run")
# load the saved NumPy array
loaded_array = np.load('file1.npy')
# display the loaded array
print(loaded_array)

"""[[ 1  3  5]
 [ 7  9 11]]"""

# Next  run
print (" Next  run")
# create a NumPy array
array2 = np.array([[1, 3, 5], 
                   [7, 9, 11]])
# save the array to a file
np.savetxt('file2.txt', array2)


# Next  run
print (" Next  run")
# load the saved NumPy array
loaded_array = np.loadtxt('file2.txt')
# display the loaded array
print(loaded_array)
"""[[1. 3. 5.]
 [7. 9. 11.]]"""


