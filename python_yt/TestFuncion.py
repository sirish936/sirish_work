class MyClass:
    @staticmethod
    def test_test(self):
        return False
 
    # @property
    # def test_test_value(self):
    #     return self.test_test()
 
# Access the property without parentheses
obj = MyClass()
print("testing", MyClass.test_test(obj))  # Output: testing False