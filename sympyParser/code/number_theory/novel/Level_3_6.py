from sympy import symbols, div

# Variables
days_old = 706
birth_day = 6  # Saturday (0=Sunday, 1=Monday, ..., 6=Saturday)

# Calculate the number of weeks and extra days
weeks, extra_days = div(days_old, 7)

# Determine the day of the week
day_of_week = (birth_day + extra_days) % 7

# Mapping numbers to days of the week
days_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

# Final answer
final_answer = days_mapping[day_of_week]
final_answer
