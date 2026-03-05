# Abstraction (access specifiers)
class A:
    def __init__(self, a, b):
        self.__a = a # private
        self._b = b # protected
class B(A):
    def test(self):
        # print(self.__a)
        print(self._b)
obj = B(3,4)
obj.test()
