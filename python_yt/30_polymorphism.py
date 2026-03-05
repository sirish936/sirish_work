# Compile-time polymorphism, Method Overloading
class A:
    def sum(self,a,b):
        return a+b
    def sum(self,a,b,c):
        return a+b+c
obj = A()
# print(obj.sum(1,2)) Not possible
print(obj.sum(1,2,3))
print(obj.sum('sirish ', 'learning ', 'Python'))

# Run-time/Dynamic polymorphism, Method Overriding
class A:
    def display(self):
        print("From A")
class B(A):
    def display(self):
        print("From B")
        super().display()
obj = B()
obj.display()

# Duck typing example
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Bird:
    def sound(self):
        return "Tweet!"

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())
make_sound(Cat())
make_sound(Bird())






