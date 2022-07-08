import numpy as np

# First array
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# --------------------------------------------------------------------------------

# Finding the data structure type of a numpy array object
# print(type(arr))

# --------------------------------------------------------------------------------

# passing a tuple, dictionary and set to see what becomes an array

# a_tuple = (1, 2, 3)
# a_dict = {'a':1, 'b':2, 'c':3}
# a_set = {1, 2, 3}

# arr1 = np.array(a_tuple)
# arr2 = np.array(a_dict)
# arr3 = np.array(a_set)

# print(arr1)
# print(arr2)
# print(arr3)

# --------------------------------------------------------------------------------

# 0D array (only 1 element)

# arr = np.array(42)
# print(arr)

# --------------------------------------------------------------------------------

# 1D array (1 row of elements)

# arr = np.array([1, 2, 3])
# print(arr)

# --------------------------------------------------------------------------------

# 2D array (has 1D row of arrays as its elements)

# arr = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
# print(arr)

# --------------------------------------------------------------------------------

# 3D array (has 2D row of arrays as its elements)

# arr = np.array([[[1, 2, 3], [2, 3, 4]], [[2, 3, 4], [3, 4, 5]]])
# print(arr)

# --------------------------------------------------------------------------------

# finding out no. of dimensions (ndim)

# a_0 = np.array(42)
# a_1 = np.array([1, 2, 3])
# a_2 = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
# a_3 = np.array([[[1, 2, 3], [2, 3, 4]], [[2, 3, 4], [3, 4, 5]]])
# print('a_0.ndim')
# print('a_1.ndim')
# print('a_2.ndim')
# print('a_3.ndim')

# --------------------------------------------------------------------------------

# higher dimension arrays (using ndmin arguement)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions : ', arr.ndim)

