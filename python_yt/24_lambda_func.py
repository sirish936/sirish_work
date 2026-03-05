def sirish(a):
    return a*a
print(sirish(5))

f = lambda a: a*a # anonymous function
print(f(5))

f = lambda a,b: a*b # anonymous function with multiple arguments, allows only one expression
print(f(5,6))