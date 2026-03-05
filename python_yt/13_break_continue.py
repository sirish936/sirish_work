for i in [1,2,3,4,5,6,7,8,9,10]:
    if(i == 3):
        print("break at ",i)
        break
print("break end")

def new_func():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        if i == 3:
            continue
        print("break",i)
    print("break end")

new_func()

def new_func1():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        if i%3==0 or i%5==0:
            continue
        print("break",i)
    print("break end")

new_func1()

def new_func2():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        if i%2!=0:
            pass
        else:
            print(i)
    print("break end")
new_func2()