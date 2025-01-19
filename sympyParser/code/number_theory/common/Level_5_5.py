from sympy import symbols, mod_inverse, simplify

# Define the modulus
modulus = 17

# Find the multiplicative inverse of 2 modulo 17
n = mod_inverse(2, modulus)

# Calculate (2^n)^2 - 2 mod 17
result = (2**n)**2 - 2
final_answer = simplify(result % modulus)

final_answer
