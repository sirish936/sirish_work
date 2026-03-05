def sirish():
    print('Function execution')
sirish()

def sirish_args(a,b):
    print('Sum is',a+b)
sirish_args(1,2)
print('function call without return ',sirish_args(1,2))

def sirish_args(a,b):
    return b-a
sirish_args(1,2)
print('function call with return ',sirish_args(1,2))

def sirish_args(a,b):
    c= a+b
    d = a*b
    return c,d
res1, res2 = sirish_args(1,2)
print('function call multiple return ',res1,res2)

def sirish_args_list(a):
    for i in a:
        print(i)
sirish_args_list([1,3,5,2,4])

def sirish_arbitary_args(*a):
    print(a)
sirish_arbitary_args(1,2,3,6,7,[1,2,3])

def sirish_kwargs(**a):
    print(a)
sirish_kwargs(name='sirish',age=30)

a = 5
b = 5
print("Test Assert")
assert a == b

def sirish(a):
    if a==10:
     return "siri"
    elif a == 5:
        return 5
print("RETURN")
print(sirish(10))
print(sirish(5))


def update(a):
    a = 10
    print(id(a))
    print("Inside function",a)
a = 5
update(a)
print(id(a))
print("Outside function",a)

lst = [1,2,3,4,5]
def update_list(lst):
    lst.append(6)
    print(id(lst))
    print("Inside function",lst)
update_list(lst)
print(id(lst))
print("Outside function",lst)

lst = [1,2,3,4,5]
def find_even_odd(lst):
    even_list =[]
    odd_list  =[]
    for i in lst:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list
    #return [i for i in lst if i % 2 == 0], [i for i in lst if i % 2 != 0]
res1, res2 = find_even_odd(lst)
#res1, res2 = list(filter(lambda x: x % 2 == 0, lst)), list(filter(lambda x: x % 2 != 0, lst))
print("Even List",res1)
print("Odd List",res2)

