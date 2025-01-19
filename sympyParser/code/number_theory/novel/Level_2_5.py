from sympy import symbols, div

# Define the total days and the number of days in a week
total_days = 270
days_in_week = 7

# Calculate the number of weeks and extra days
weeks, extra_days = div(total_days, days_in_week)

# Define the starting day (Monday)
starting_day = 0  # Monday

# Calculate the final day of the week
final_day = (starting_day + extra_days) % days_in_week

# Map the final day to the corresponding day name
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
final_answer = days_of_week[final_day]

final_answer
