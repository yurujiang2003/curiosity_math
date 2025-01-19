from sympy import symbols, simplify

# Define the number of choices for each digit
hundreds_choices = 4  # 6, 7, 8, 9
tens_choices = 3      # 5, 6, 7
units_choices = 1     # 2

# Calculate the total number of three-digit numbers
total_numbers = hundreds_choices * tens_choices * units_choices

# Return the final answer
total_numbers
