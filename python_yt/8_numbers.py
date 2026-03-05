# Convert binary to decimal number examples

# Method 1: Using int() with base 2
binary_str = "1010"
decimal = int(binary_str, 2)
print(f"Binary {binary_str} = Decimal {decimal}")  # Output: 10

# Method 2: Using int() with 0b prefix
binary_with_prefix = "0b1111"
decimal = int(binary_with_prefix, 2)
print(f"Binary {binary_with_prefix} = Decimal {decimal}")  # Output: 15

# Method 3: Direct binary literal
binary_literal = 0b1101
print(f"Binary 0b1101 = Decimal {binary_literal}")  # Output: 13

# Method 4: Multiple examples
binaries = ["1000", "10101", "11111111", "1"]
for binary in binaries:
    decimal = int(binary, 2)
    print(f"Binary {binary} = Decimal {decimal}")

# Method 5: Manual conversion (educational)
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

binary = "1010"
result = binary_to_decimal(binary)
print(f"\nManual conversion: Binary {binary} = Decimal {result}")

# Convert decimal to binary number examples

# Method 1: Using bin() function
decimal_num = 10
binary = bin(decimal_num)
print(f"\nDecimal {decimal_num} = Binary {binary}")  # Output: 0b1010

# Method 2: Using bin() and removing '0b' prefix
decimal_num = 15
binary = bin(decimal_num)[2:]
print(f"Decimal {decimal_num} = Binary {binary}")  # Output: 1111

# Method 3: Using format() function
decimal_num = 13
binary = format(decimal_num, 'b')
print(f"Decimal {decimal_num} = Binary {binary}")  # Output: 1101

# Method 4: Using f-string formatting
decimal_num = 8
binary = f"{decimal_num:b}"
print(f"Decimal {decimal_num} = Binary {binary}")  # Output: 1000

# Method 5: Multiple examples
decimals = [8, 21, 255, 1]
for decimal_num in decimals:
    binary = bin(decimal_num)[2:]
    print(f"Decimal {decimal_num} = Binary {binary}")

# Method 6: Manual conversion (educational)
def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    binary = ""
    while decimal_num > 0:
        binary = str(decimal_num % 2) + binary
        decimal_num = decimal_num // 2
    return binary

decimal_num = 10
result = decimal_to_binary(decimal_num)
print(f"\nManual conversion: Decimal {decimal_num} = Binary {result}")

# Decimal to Octal and Hexadecimal conversions
print("\n--- Decimal to Octal and Hexadecimal ---")
decimal_num = 255
octal = oct(decimal_num)[2:]  # Remove '0o' prefix
hexadecimal = hex(decimal_num)[2:]  # Remove '0x' prefix
print(f"Decimal {decimal_num} = Octal {octal} = Hexadecimal {hexadecimal}")

# Binary to Octal and Hexadecimal conversions
print("\n--- Binary to Octal and Hexadecimal ---")
binary_str = "11111111"
decimal_from_binary = int(binary_str, 2)
octal = oct(decimal_from_binary)[2:]
hexadecimal = hex(decimal_from_binary)[2:]
print(f"Binary {binary_str} = Octal {octal} = Hexadecimal {hexadecimal}")

# Octal to Decimal and Binary conversions
print("\n--- Octal to Decimal and Binary ---")
octal_str = "377"
decimal_from_octal = int(octal_str, 8)
binary = bin(decimal_from_octal)[2:]
print(f"Octal {octal_str} = Decimal {decimal_from_octal} = Binary {binary}")

# Hexadecimal to Decimal and Binary conversions
print("\n--- Hexadecimal to Decimal and Binary ---")
hex_str = "FF"
decimal_from_hex = int(hex_str, 16)
binary = bin(decimal_from_hex)[2:]
print(f"Hexadecimal {hex_str} = Decimal {decimal_from_hex} = Binary {binary}")