from sympy import Mod

# Define the numbers
numbers = [91145, 91146, 91147, 91148]

# Calculate the remainders and their sum
remainders_sum = sum(Mod(num, 4) for num in numbers)

# Find the final remainder when the sum of remainders is divided by 4
final_remainder = Mod(remainders_sum, 4)

final_remainder
