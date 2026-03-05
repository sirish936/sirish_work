import math

# Basic arithmetic functions
print("abs(-5):", abs(-5))  # Absolute value
print("pow(2, 3):", pow(2, 3))  # Power
# print("power of (2, 3):", (2**3))  # Power
print("round(3.14159, 2):", round(3.14159, 2))  # Rounding

# Math module functions
print("\n--- Trigonometric Functions ---")
print("math.sin(math.pi/2):", math.sin(math.pi/2))
print("math.cos(0):", math.cos(0))
print("math.tan(math.pi/4):", math.tan(math.pi/4))

print("\n--- Inverse Trigonometric ---")
print("math.asin(1):", math.asin(1))
print("math.acos(0):", math.acos(0))
print("math.atan(1):", math.atan(1))

print("\n--- Logarithmic Functions ---")
print("math.log(10):", math.log(10))  # Natural log
print("math.log10(100):", math.log10(100))  # Base 10
print("math.log2(8):", math.log2(8))  # Base 2

print("\n--- Exponential Functions ---")
print("math.exp(2):", math.exp(2))  # e^x
print("math.sqrt(16):", math.sqrt(16))  # Square root
print("math.pow(2, 3):", math.pow(2, 3))  # Power

print("\n--- Rounding Functions ---")
print("math.ceil(3.2):", math.ceil(3.2))  # Round up
print("math.floor(3.8):", math.floor(3.8))  # Round down
print("math.trunc(3.9):", math.trunc(3.9))  # Truncate

print("\n--- Other Functions ---")
print("math.factorial(5):", math.factorial(5))
print("math.gcd(48, 18):", math.gcd(48, 18))  # Greatest common divisor
print("math.degrees(math.pi):", math.degrees(math.pi))  # Radians to degrees
print("math.radians(180):", math.radians(180))  # Degrees to radians
print("math.isnan(float('nan')):", math.isnan(float('nan')))
print("math.isinf(float('inf')):", math.isinf(float('inf')))

print("\n--- Constants ---")
print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.tau:", math.tau)
print("math.inf:", math.inf)