def add(a, b):
    return a + b
print(add(1, 2))

def person(name, age):
    print(f"Name: {name}, Age: {age}")
person("Sirish", 30)
person(30, "Sirish",) # This will work but the order of arguments is not correct

def person(name, age):
    print(f"Name: {name}, Age: {age}")
person(name="Sirish", age=30) # This is the correct way to call the function with keyword arguments
person(age=30, name="Sirish") # This will also work as the order of arguments is not important when using keyword arguments

def person(name, age=32):
    print(f"Name: {name}, Age: {age}")
person("Sirish") # This will use the default value of age

def add(a, *b):
    print(a)
    print(b)
    c = 0
    for i in b:
        c += i
    return a + c
print(add(1, 2, 3, 4))

def sirish_arbitary_args(*a):
    print(a)
sirish_arbitary_args(1,2,3,6,7,[1,2,3])# variable length arguments


def sirish_kwargs(**a):
    print(a)
    for key, value in a.items():
        print(f"{key}: {value}")
sirish_kwargs(name='sirish',age=30)# keyword arguments
