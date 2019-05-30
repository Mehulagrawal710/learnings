"""NUMPY ARRAYS AS COMPARED TO LISTS IN PYTHON, TAKES SIGNIFICANTLY
MUCH LESSER STORAGE SPACE AND COMPUTATION TIME"""

import numpy as np
import matplotlib.pyplot as plt

#declaring numpy array
a = np.array([1, 2, 3])
a = np.array([[1, 2, 3], [4, 5, 6]])

#arange function 
a = np.arange(100)

#get the dimension of array
print(a.ndim)

#get size of element in the array in bytes
print(a.itemsize)

#datatype of array
print(a.dtype)

#size of array(total no. of elements in array)
print(a.size)

#shape of array
print(a.shape)

#reshaping array
#reshape(row, col)
a = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
a = a.reshape(4, 2)
print(a)

#slicing array
#a[row1:row2, col1:col2]
a = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]])
print(a[0, 2])
print(a[0:2, 1:3])

#equally seperated values between limits
#linspace(start limit inclusive, end limit inclusive, steps)
a = np.linspace(1, 3, 10)
print(a)

#vectorized sum
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a+b)

#vectorized subtraction
print(a-b)

#vectorized multiplication
print(a*b)

#vectorized division
print(a/b)

#concatinating arrays
#vertical concatination
print(np.vstack((a, b)))
#horizontal concatination
print(np.hstack((a, b)))

#converting multi-dim array to a single column
print(a.ravel())

#maximum element in array
print(a.max())

#minimum element in array
print(a.min())

#sum of all elements in array
print(a.sum())

#getting sum of each column as a list
#for columns, axis = 0
print(a.sum(axis=0))

#getting sum of each row as a list
#for rows, axis = 1
print(a.sum(axis=1))

#sqr root
print(np.sqrt(a))

#standard deviation
print(np.std(a))

#trignometric functions
x = np.arange(0, 3*np.pi, 0.1)

#sine function
y = np.sin(x)
plt.plot(x, y)
plt.show()

#cosine function
y = np.cos(x)
plt.plot(x, y)
plt.show()

#tan function
y = np.tan(x)
plt.plot(x, y)
plt.show()

#exponential, log functions
a = np.array([1, 2, 3])
print(np.exp(a))

print(np.log(a))

print(np.log10(a))