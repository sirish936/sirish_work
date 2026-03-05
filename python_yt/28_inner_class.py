class OuterClass:
    """Outer class example"""
    
    def __init__(self):
        self.outer_var = "Outer variable"
        self.inner = self.InnerClass()
    
    def outer_method(self):
        print(f"Outer method called: {self.outer_var}")
    
    class InnerClass:
        """Inner class definition"""
        
        def __init__(self):
            self.inner_var = "Inner variable"
        
        def inner_method(self):
            print(f"Inner method called: {self.inner_var}")


# Creating an instance of outer class
outer = OuterClass()
outer.outer_method()

# Accessing inner class through outer instance
outer.inner.inner_method()

# Creating inner class directly
inner_direct = OuterClass.InnerClass()
inner_direct.inner_method()