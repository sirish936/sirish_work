a = 5
d = 2
def scope_test():
    # global a
    a = 10
    b = 15
    print(a)
    print(d)
scope_test()
print(a)
# print(b)


# global and local variable name in same function
a = 5
print(id(a))
def scope_test():
    a = 10
    print(a)
    x = globals()['a']
    
    print(id(x))
    print("Global a", x)
scope_test()
print(a)

