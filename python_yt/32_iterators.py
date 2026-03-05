class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration


# Usage
counter = CountUp(5)
for num in counter:
    print(num)

# Generator example
def count_up_generator(max):
    current = 0
    while current < max:
        current += 1
        yield current

# Usage
for num in count_up_generator(5):
    print(num)