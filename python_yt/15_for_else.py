# for-else example
# The else block executes when the loop completes normally (without break)

# Example 1: Search for a number
numbers = [1, 3, 5, 7, 9]
search_for = 4

for num in numbers:
    if num == search_for:
        print(f"Found {search_for}!")
        break
else:
    print(f"{search_for} not found in the list")

import math
# Example 2: Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} is not prime, divisible by {i}")
            break
    else:
        print(f"{n} is prime")
        return True
    return False


is_prime(17)
is_prime(20)

print(16 ** 0.5)

# Example 3: Print all prime numbers in a range
def print_primes(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            print(f"{num} is prime")

print_primes(1, 30)