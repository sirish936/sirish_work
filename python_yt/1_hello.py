print('Hello Python!')
# variable
a=10
print(a)
a="sirish"
print(a)
# Rules for variable names
# 1. variable names shouldn't start with numbers, symbols
# 1hello=10
# print(1hello)
# @hello="sirish"
# print(@hello)
# 2. keyword names can't be used as variable names
# while="keyword"
# print(while)
a=b=c=10
print(a)
print(b)
print(a,b,c)
a,b,c=1,2,3
print(b)
print(a,b,c)
print('a, b, c values are:',a,b,c)
print('a value is {}, b value is {}, c value is {}'.format(a,b,c))
print('a value is {first}, b value is {second}, c value is {third}'.format(first=a,second=b,third=c))
print('b value is {second}, a value is {first}, c value is {third}'.format(first=a,second=b,third=c))
d=a+c
print(d)
_sirish = 20
print(_sirish)
print(type(_sirish))
