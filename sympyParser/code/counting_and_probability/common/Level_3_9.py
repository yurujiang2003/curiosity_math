from sympy import factorial

# Define the number of choices
choices_driver = 2  # M or W
choices_front_passenger = 3  # W, C2, C3 or M, C2, C3
arrangements_back = factorial(3)  # 3!

# Calculate total arrangements
total_arrangements = choices_driver * choices_front_passenger * arrangements_back
total_arrangements
