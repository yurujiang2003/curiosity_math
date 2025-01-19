from sympy import symbols, mod

# Define the numbers
a = 91145
b = 91146
c = 91147
d = 91148

# Calculate the remainders
remainder_a = mod(a, 4)
remainder_b = mod(b, 4)
remainder_c = mod(c, 4)
remainder_d = mod(d, 4)

# Sum the remainders
total_remainder = remainder_a + remainder_b + remainder_c + remainder_d

# Find the final remainder when divided by 4
final_remainder = mod(total_remainder, 4)

final_remainder
