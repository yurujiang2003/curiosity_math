from sympy import symbols, mod

# Define the smallest three-digit number
num = 100

# Check the modulo and find the next number that is congruent to 1 (mod 7)
while mod(num, 7) != 1:
    num += 1

# Return the final answer
num
