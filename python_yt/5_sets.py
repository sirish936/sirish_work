# Set is faster than list
# Set is unordered collection
# Set won't output any duplicates entered
# Set doesn't work on index based, because it is unordered collection, we can't access set elements by index
a = {}
print(type(a))
a = {1,2,5,7,8,'sirish',8}
print(type(a))
print(a)
print(len(a))
a.add('learn')
print(a)
print(len(a))
# print(a[5])
b = {2,7, 3+2j, 'python'}
# set with unique elements between 2
print("Hello_0")
print(b-a)
print(a-b)
print(a.difference(b))
print('python' in b)
# set intersection
print("Hello_1")
print(a & b)
print(a.intersection(b))
print("Hello_2")
print(a and b) # returns the last evaluated value, if all values are true, it returns the last value, if any value is false, it returns the first false value
print(b and a) # returns the last evaluated value, if all values are true, it returns the last value, if any value is false, it returns the first false value
# set union/common
print("Hello_3")
print(a | b)
print(a.union(b))
print(a or b)
print(a)
print(a ^ b) # elements in a and b but not in both
print(a.isdisjoint(b))

y=101
x = 1 if y == 10 else 5
print (x)
