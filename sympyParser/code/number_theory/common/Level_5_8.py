from sympy import symbols, Eq, solve, S
from itertools import permutations

# Define the two-digit numbers as variables
a, b, c, d = symbols('a b c d')

# Equation for the sum of the four two-digit numbers
equation = Eq(a + b + c + d, 221)

# Generate all possible two-digit numbers using digits 1 to 9
two_digit_numbers = [10 * i + j for i in range(1, 10) for j in range(1, 10) if i != j]

# Find valid combinations of four two-digit numbers
valid_combinations = []
for combo in permutations(two_digit_numbers, 4):
    if sum(combo) == 221:
        digits_used = set()
        for number in combo:
            digits_used.update(str(number))
        if len(digits_used) == 8:  # Ensure all digits are unique
            valid_combinations.append(digits_used)

# Identify which digits from 1 to 9 are not used
all_digits = set('123456789')
used_digits = set.union(*valid_combinations)
missing_digits = all_digits - used_digits

# Return the missing digit
missing_digits
