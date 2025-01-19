from sympy import symbols, Add

# Define the percentages
p7_days = 40
p5_6_days = 30
p1_4_days = 20

# Calculate the total percentage of households eating dinner together at least once a week
total_percentage = Add(p7_days, p5_6_days, p1_4_days)

# Return the final answer
total_percentage
