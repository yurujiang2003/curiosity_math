from sympy import Mod

# Define the number of days to add and the starting day of the week
days_to_add = 270
starting_day = 0  # Monday

# Calculate the extra days after full weeks
extra_days = Mod(days_to_add, 7)

# Determine the final day of the week
final_day = (starting_day + extra_days) % 7

# Map the final day to the corresponding day name
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
final_answer = days_of_week[final_day]

final_answer
