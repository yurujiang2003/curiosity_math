from sympy import lcm

# Define the intervals
watering_interval = 9
feeding_interval = 60

# Calculate the LCM of the two intervals
next_watering_feeding = lcm(watering_interval, feeding_interval)

# Calculate the day of the week
days_in_week = 7
days_after_tuesday = next_watering_feeding % days_in_week

# Days of the week starting from Tuesday
days_of_week = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday"]

# Determine the next day
next_day = days_of_week[(days_after_tuesday + 1) % days_in_week]

next_day
