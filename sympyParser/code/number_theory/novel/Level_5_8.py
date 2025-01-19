from sympy import symbols, Eq, solve, N
from itertools import permutations

# Define the variables for the two-digit numbers
a, b, c, d = symbols('a b c d')

# Define the equation for the sum of the four numbers
equation = Eq(a + b + c + d, 221)

# Generate all permutations of digits from 1 to 9
digits = '123456789'
valid_combinations = []

# Check all combinations of four two-digit numbers
for perm in permutations(digits, 8):
    num1 = int(perm[0] + perm[1])
    num2 = int(perm[2] + perm[3])
    num3 = int(perm[4] + perm[5])
    num4 = int(perm[6] + perm[7])

    if num1 + num2 + num3 + num4 == 221:
        valid_combinations.append((num1, num2, num3, num4))

# Find the digits used in the valid combinations
used_digits = set()
for combination in valid_combinations:
    for number in combination:
        used_digits.update(str(number))

# Determine the missing digits
all_digits = set(digits)
missing_digits = all_digits - used_digits

# Return the smallest missing digit
final_answer = min(missing_digits)
final_answer
