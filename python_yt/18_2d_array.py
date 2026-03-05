from numpy import *

arr = array([[1, 2, 3],[3, 4, 5]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr[0])
print(arr[1])

arr2 = arr.flatten()
print(arr2)

arr3 = array([[1, 2, 3,4,5,6],[3, 4, 5,6,7,8]])
arr4 = arr3.flatten()
arr5 = arr4.reshape(3, 4)
print(arr5)
arr6 = arr4.reshape(2,2,3)
print(arr6)

arr7 = array([[1, 2, 3],[3, 4, 5]])
m = arr7.max()
print(m)

m = matrix(arr7)
print(m)

m = matrix('1 2 3; 3 4 5; 5 6 7')
print(m)
print(diagonal(m))

m1 = matrix('1 2; 3 4')
m2 = matrix('1 3; 1,2')
m3 = m1 + m2
print(m3)

m3 = m1 * m2
print(m3)

arr8 = array([[1, 2, 3,4,5,6],[3, 4, 5,6,7,8],[1, 2, 3,4,5,6]])
print(arr8[0:2,0:2])
print(arr8[:,:])
print(arr8[0:,0:2])
print(arr8[1:2,3:5])