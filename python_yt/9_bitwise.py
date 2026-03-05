# Bitwise Operations in Python

a = 10  # Binary: 1010
b = 4   # Binary: 0100

# AND (&) - Both bits must be 1
print(f"AND: {a} & {b} = {a & b}")  # 0

# OR (|) - At least one bit must be 1
print(f"OR: {a} | {b} = {a | b}")  # 14

# XOR (^) - Bits must be different
print(f"XOR: {a} ^ {b} = {a ^ b}")  # 14

# NOT (~) - Inverts all bits
print(f"NOT: ~{a} = {~a}")  # -11

# Left Shift (<<) - Shifts bits left, fills with 0
print(f"Left Shift: {a} << 2 = {a << 2}")  # 40

# Right Shift (>>) - Shifts bits right
print(f"Right Shift: {a} >> 2 = {a >> 2}")  # 2