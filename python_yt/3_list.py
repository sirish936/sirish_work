# list is mutable, we can change values in list
a = [1,'sirish',True,2.2]
print(type(a))
print(a)
print(a[0])
print(a[2])
print(len(a))
a[3] = 'insert'
print(a)

b = [2, 'python', a]
print(b)
print(b[2][1])
print(b[2][2])

a.append('six')
print(a)
print(len(a))

a.extend(b)
print(a)
print(len(a))

a.insert(3,'learn')
print(a)
print(len(a))

print(a.index('sirish'))

c = [1,'sirish',True,2.2]

print(c[1:3])
print(c[1:10])
print(c[1:])
print(c[:3])
print(c[-1])
print(c[-2])
print(c[-2:])
print(c[:-1])
print(c[-1:-4])



a.pop(2)
print(a)
c.pop()
print(c)
print(len(a))
#a.remove(2.2)
print(a)

d = [6,1,2,3,4,5]

print(sum(d))
print(min(d))
print(max(d))

d.sort()
print(d)

# print(sum(a))
