from sympy import symbols, div

# Define the total days
total_days = 706

# Calculate weeks and extra days
weeks, extra_days = div(total_days, 7)

# Define the days of the week starting from Saturday
days_of_week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Calculate the day of the week after extra_days
final_day = days_of_week[(0 + extra_days) % 7]

# Return the final answer
final_day
