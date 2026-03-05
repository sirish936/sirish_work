def fib(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a, b = b, a + b
            print(c)

n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib(n)

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter the number of Fibonacci numbers to generate: "))
for i in range(n):
    print(fib(i))

