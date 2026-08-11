import numpy as np

# arr = np.array([])
# print(arr)
# print(type(arr))

#strides means ik elements se next element me kitni bytes lgi hai ya memory lgi
#single array
# arr = np.array([1,2,3,4,5], dtype=np.uint32)  # dtype is used to specify the data type of the array elements

#multi-dimensional array

# myList = [
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#     [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     [[19, 20, 21], [22, 23, 24], [25, 26, 27]]
#     ]

# arr = np.array(myList,dtype=np.uint32)  # dtype is used to specify the data type of the array elements

# print("Array ", arr)
# print("Array shape ", arr.shape)  # shape of the array
# print("Array size ", arr.size)  # size of the array
# print("Array ndim ", arr.ndim)  # number of dimensions of the array
# print("Array dtype ", arr.dtype)  # data type of the array elements
# print("Array itemsize ", arr.itemsize)  # size of each element in bytes
# print("Array nbytes ", arr.nbytes)  # total size of the array in bytes
# print("Array strides ", arr.strides)  # number of bytes to step in each dimension when traversing an array
# print("Array data ", arr.data)  # buffer containing the actual elements of the array
# print("Arr.Flags ", arr.flags)  # information about the memory layout of the array


# zero method in numpy is used to create an array of given shape and type, filled with zeros.
# arr = np.zeros((3, 4), dtype=np.uint32)  # create

#ones method in numpy is used to create an array of given shape and type, filled with ones.
# arr = np.ones((3, 4), dtype=np.uint32)  # create

#np.empty method in numpy is used to create an array of given shape and type, without initializing the entries.
# arr = np.empty((3, 4), dtype=np.uint32)  # create

#full method in numpy is used to create an array of given shape and type, filled with a specified value.
# arr = np.full((3, 4), 7, dtype=np.uint32)  # create

#eye method in numpy is used to create a 2-D array with ones on the diagonal and zeros elsewhere.
# arr = np.eye(4, 3, dtype=np.uint32)  # create
#float is default data type in numpy, if we don't specify the data type, it will be float.

#fromstring method in numpy is used to create an array from a string representation of the array.
# arr = np.fromstring("1 2 3 4 5", dtype=np.uint32, sep=' ')  # create

# np.arange method in numpy is used to create an array with evenly spaced values within a given interval.
# arr = np.arange(1, 10, 2, dtype=np.uint32)  # creates

#linespace 50 by default elements create kr de ga between the numbers evenly spaced 
# arr = np.linspace(1, 2)

5
