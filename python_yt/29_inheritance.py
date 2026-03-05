# Single Inheritance
class Parent:
    def fun1(self):
        print('This is from Parent')

class Child(Parent):
    def fun2(self):
        print('This is from Child')
obj = Child()
obj.fun2()
obj.fun1()

# Multilevel Inheritance
class Parent:
    def fun1(self):
        print('This is from Parent')

class Child(Parent):
    def fun2(self):
        print('This is from Child')

class GrandChild(Child):
    def fun3(self):
        print('This is from GrandChild')
obj = GrandChild()
obj.fun2()
obj.fun1()
obj.fun3()

obj = Child()
# obj.fun3() Not possible

# Hierarical Inheritance
class Parent:
    def fun1(self):
        print('This is from Parent')

class Child1(Parent):
    def fun2(self):
        print('This is from Child1')

class Child2(Parent):
    def fun3(self):
        print('This is from Child2')

obj = Child1()
obj.fun1()
obj.fun2()
# obj.fun3() Not possible

# Multiple Inheritance
class Father:
    def fun1(self):
        print('This is from Father')

class Mother:
    def fun2(self):
        print('This is from Mother')

class Child(Father, Mother):
    def fun3(self):
        print('This is from Child')

obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()

# Super
class A:
    def __init__(self):
        print("From class A")

class B(A):
    def __init__(self):
        print("From class B")
        super().__init__()

obj = B()
obj.__init__()

# Multiple Inheritance, how python overcome it ? [Depending on the order of the classes inherited in Child class]
class Father:
    def fun1(self):
        print('This is from Father')

class Mother:
    def fun1(self):
        print('This is from Mother')

class Child1(Mother, Father):
    def fun3(self):
        print('This is from Child1')

class Child2(Father, Mother):
    def fun4(self):
        print('This is from Child2')

obj = Child1()
obj.fun1()

obj = Child2()
obj.fun1()
