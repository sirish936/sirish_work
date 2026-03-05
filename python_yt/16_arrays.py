import array
arry = array.array('i', [1, 9, 3, 4, 5]) 
print(arry)
print(arry[2])
print(len(arry))
print(arry.index(1))
print(arry.index(9))
print(arry.index(3))

print(arry*2)
print(arry.buffer_info())
print(arry.typecode)

c_arr = array.array('u', ['a', 'b', 'd', 'c', 'x']) 


for i in range(5):
    print(arry[i])

for i in range(len(c_arr)):
    print(c_arr[i])

for char in c_arr:
    print(char)

i = 0
while i < len(arry):
    print(arry[i])
    i += 1

print('sorted(arry)')
print(sorted(arry))
print(max(arry))
print(min(arry))
print(sum(arry))
print(arry.append(6))
print(arry)
      

newArry = array.array(arry.typecode, (x for x in arry))
for i in newArry:
    print(i)

newArry = array.array(arry.typecode, (x*2 for x in arry))
for i in newArry:
    print(i)

newArry = array.array(arry.typecode, (x**2 for x in arry))
for i in newArry:
    print(i)

# Read the length of the array from user input
n= int(input("Enter the length of the array: "))
arry = array.array('i', [])  # Create an empty array of integers

for i in range(n):
    e = int(input("Enter element: "))
    arry.append(e)
print(arry)

val = int(input("Enter the element to search: "))

k = 0
for i in arry:
    if val == i:
        print("Element found at index:", k) 
        break
    k += 1        
 
print("Element is in the index:", arry.index(val))

    