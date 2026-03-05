# tuple is immutable, we cannot change values in tuple
T=()
print(type(T))
T=(1,2.2,'sirish',True)
print(T[2])
print(len(T))
print(T.index('sirish'))

# T[2] = 110
# print(T)
# print(len(T))

# since tuple is immutable, it takes less memory and we can not change values in tuple, iteration is faster in tuple than list

# membership
print('sirish' in T)
print('ramesh' in T)

# repetations
print(T*2)

# concatination
U=('tuple','concat')
print(T+U)
print(len(T))
print(len(U))
print(len(T+U))

# print(min(T))

# iterations
for i in T:
    print(i)

T=(12,3,4,5,6,7,8,9,10)
print(min(T))
print(max(T))
print(sum(T))
print(sorted(T))

