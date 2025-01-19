from sympy import Rational

# Define the percentages
percent_7_days = Rational(40, 100)
percent_5_6_days = Rational(30, 100)
percent_1_4_days = Rational(20, 100)

# Calculate the total percentage of households eating together at least once a week
total_percentage = percent_7_days + percent_5_6_days + percent_1_4_days

# Return the final answer as a percentage
total_percentage.evalf() * 100
