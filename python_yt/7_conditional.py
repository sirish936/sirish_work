if True:
    print('this is if')

    if False:
        print('this is false')

a,b=1,3
if a<b:
    print('a is smaller than b')
else:
    print('b is smaller than a')

a,b,c=1,3,4
if a<b:
    print('a is smaller than b')
elif b<c:
    print('b is smaller than c')
else:
    print('c is greater than a and b')

a,b,c=5,3,4
if a<b: print('a is smaller than b')
elif b<c: print('b is smaller than c')
else: print('c is greater than a and b')

a,b,c=200,33,500
if a>b and c>b:
    print("Logical and")
else:
    print("Logical and-else")

a,b,c=200,33,500
if a>b or b>c:
    print("Logical or")
else:
    print("Logical and-else")

if a>b:
    pass

a = True
if(a):
    print("PRASANNA")