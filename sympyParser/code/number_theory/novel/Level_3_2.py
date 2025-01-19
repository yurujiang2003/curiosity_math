from sympy import symbols, div

# Define variables
total_days = 200
days_in_week = 7
today = "Wednesday"

# Calculate complete weeks and remaining days
weeks, remainder = div(total_days, days_in_week)

# Calculate the day of the week for Kim's birthday
days_back = remainder
week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
today_index = week_days.index(today)

# Find the index of Kim's birthday
birthday_index = (today_index - days_back) % days_in_week

# Get the day of the week for Kim's birthday
birthday_day = week_days[birthday_index]
birthday_day
