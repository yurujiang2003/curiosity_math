from sympy import symbols, mod_inverse, simplify

# Define the modulus and the base
modulus = 17
base = 2

# Find the multiplicative inverse of 2 modulo 17
n = mod_inverse(base, modulus)

# Calculate (2^n)^2 - 2 mod 17
result = (base**n)**2 - 2
final_answer = simplify(result % modulus)

final_answer
