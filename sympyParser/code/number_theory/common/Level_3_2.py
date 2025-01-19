from sympy import Mod

# Define the number of days and the current day
days_passed = 200
current_day_index = 3  # Wednesday (0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday)

# Calculate the remainder when dividing by 7
remainder_days = Mod(days_passed, 7)

# Calculate the day index of Kim's birthday
birthday_day_index = Mod(current_day_index - remainder_days, 7)

# Define the days of the week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Get the day of the week for Kim's birthday
birthday_day = days_of_week[birthday_day_index]

birthday_day
