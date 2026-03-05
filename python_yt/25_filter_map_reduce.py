from functools import reduce

def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(is_even, nums))
print(even_nums)
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

squared_nums = list(map(lambda x: x*x, nums))
print(squared_nums)

sum_nums = reduce(lambda x, y: x+y, nums)
print(sum_nums)