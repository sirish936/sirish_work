#import array
import numpy as np
from numpy import *
# 1. Create a 1D array
# arr = array.array([1, 2, 3, 4, 5])
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)
arr = array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)
arr2 = np.array([[1, 2, 3, 4, 5],[1, 2 , 3, 4, 5]])
print(arr2)

arr = linspace(0, 10, 5)
print(arr)

arr = linspace(0, 10, 10)
print(arr)

arr = linspace(0, 10, 9)
print(arr)

arr = arange(0, 10, 2)
print(arr)

arr = logspace(1, 20, 5)
print(arr)
print(arr[1])

arr = zeros((2))
print(arr)

arr = ones((2))
print(arr)

arr = ones((2),int)
print(arr)

#add 5 to eah element
# traditional way
arr = np.array([1, 2, 3, 4, 5])
for i in range(len(arr)):
    arr[i] += 5
print(arr)
# using vectorized operations
arr = arr + 5
print(arr)

print(sum(arr))
print(sin(arr))
print(cos(arr))
print(log(arr))
print(min(arr))
print(concatenate((arr, arr)))

arr2 = arr
print(arr2)
print(arr)
print(id(arr))
print(id(arr2))

arr3 = arr.view()
print(arr3)
print(arr)
print(id(arr))
print(id(arr3))

#shallow copy
arr2 = arr
arr[2] = 100
print(arr2)
print(arr)
print(id(arr))
print(id(arr2))

#deep copy
arr1 = np.array([1, 2, 5, 4, 9])
arr4 = arr1.copy()
arr1[2] = 100
print(arr1)
print(arr4)
print(id(arr1))
print(id(arr4))

l = [1,2,3,4,5,6,7,8,9]
arr = array(l)
val = 3
arr = arr[arr > val]
print(arr)

arr = arr > val
print(arr)
