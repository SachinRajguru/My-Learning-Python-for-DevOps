# Task 5: Bitwise Operators (Optional)

# Bitwise operators work on the binary representation of integers

a = 10  # Binary: 1010
b = 4   # Binary: 0100

# Bitwise AND (&) - sets each bit to 1 if both bits are 1
and_result = a & b  # 1010 & 0100 = 0000
print("a & b:", and_result)  # Output: 0

# Bitwise OR (|) - sets each bit to 1 if one of the bits is 1
or_result = a | b   # 1010 | 0100 = 1110
print("a | b:", or_result)  # Output: 14

# Bitwise XOR (^) - sets each bit to 1 if only one of the bits is 1
xor_result = a ^ b  # 1010 ^ 0100 = 1110
print("a ^ b:", xor_result)  # Output: 14

# Bitwise NOT (~) - inverts all the bits
not_result = ~a     # ~1010 = -1011 (in decimal, using two's complement)
print("~a:", not_result)  # Output: -11

# Left Shift (<<) - shifts bits to the left by specified positions
left_shift = a << 2  # 1010 << 2 = 101000
print("a << 2:", left_shift)  # Output: 40

# Right Shift (>>) - shifts bits to the right by specified positions
right_shift = a >> 1  # 1010 >> 1 = 0101
print("a >> 1:", right_shift)  # Output: 5