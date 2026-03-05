def div(a,b):
    return a/b

print(div(10,2))
print(div(2,10)) #In this case we will get 0.2 as output, which is a float value. 
# But we wanted always positive, i.e if numerator < denominator, swap it and execute the function

def div(a,b):
    if a < b:
        a, b = b, a
    return a/b
print(div(2,10)) #But, what if we want to swap the arguments without changing the original function ?
# Or assume we don't have access to the actual function, but we want to change the behavior of existing function, we can use a decorator for that

def smart_div(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner
new_div = smart_div(div)
#print(new_div(2,10))

@smart_div
def div(a,b):
    return a/b
print(div(2,10))