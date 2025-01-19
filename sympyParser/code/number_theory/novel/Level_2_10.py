from sympy import mod

# Define the values
a = 289
b = 9 * 51
c = 3**6
d = 4 * 187
modulus = 17

# Calculate each term modulo 17
remainder_a = mod(a, modulus)
remainder_b = mod(b, modulus)
remainder_c = mod(c, modulus)
remainder_d = mod(d, modulus)

# Sum the remainders
final_remainder = remainder_a + remainder_b + remainder_c + remainder_d

# Return the final answer modulo 17
final_result = mod(final_remainder, modulus)
final_result
