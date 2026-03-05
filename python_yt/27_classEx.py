class Example:
    a = 1 #class variable
    def method(self):
        b = 2 #local variable
        c = 3 #instance variable
        #print('sum is',a+c)
        print('sum is',self.a+c)
example_obj = Example()
example_obj.method()
print(example_obj.a)
Example.a = 10
print(example_obj.a)
Example.method(example_obj)
# print(example_obj.c)

class Mobile:
    def __init__(self,brand,camera,ram,battery,price):
        self.brand = brand
        self.camera = camera
        self.ram = ram
        self.battery = battery
        self.price = price

    def display(self): #instance method
            print('Brand:',self.brand)
            print('Camera:',self.camera)
            print('Ram:',self.ram)
            print('Battery:',self.battery)
            print('Prices:',self.price)

obj = Mobile('Apple','12MP','8GB','2000MAH','25000')
obj.display()
Mobile.display(obj)

obj_1 = Mobile('Samsung','12MP','8GB','2000MAH','8000')
obj_1.display()

class ConstructorExample:
     def __init__(self):
          print("From Constructor")
     def display(self):
        print("From method")
obj = ConstructorExample()

class Example:
    a = 1 #class variable
    def method(self):
        b = 2 #local variable
        c = 3 #instance variable
        #print('sum is',a+c)
        print('sum is',self.a+c)
    
    @classmethod #class method
    def method_2(cls):
         return cls.a
    
    @staticmethod #static method
    def method_3():
        return "This is static method"

example_obj = Example()
example_obj.method()
print(example_obj.a)
print(Example.method_2())
print(Example.method_3())
