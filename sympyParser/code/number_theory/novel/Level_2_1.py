from sympy import lcm, mod

# Define the watering and feeding intervals
watering_interval = 9
feeding_interval = 60

# Calculate the LCM of the two intervals
next_watering_feeding_day = lcm(watering_interval, feeding_interval)

# Calculate the day of the week after the given number of days
days_passed = mod(next_watering_feeding_day, 7)

# Define the starting day (Tuesday = 2)
starting_day = 2

# Calculate the next day of the week
next_day = (starting_day + days_passed) % 7

# Map the result to the corresponding day of the week
days_of_week = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
final_answer = days_of_week[next_day]

final_answer
