from sympy import binomial, gcd

# Define the number of red and green peppers
red_peppers = 10
green_peppers = 5
total_peppers = red_peppers + green_peppers
peppers_to_select = 6

# Total ways to select 6 peppers from 15
total_ways = binomial(total_peppers, peppers_to_select)

# Scenario 1: Selecting 4 green and 2 red
ways_scenario_1 = binomial(green_peppers, 4) * binomial(red_peppers, 2)

# Scenario 2: Selecting 5 green and 1 red
ways_scenario_2 = binomial(green_peppers, 5) * binomial(red_peppers, 1)

# Total ways for at least 4 green peppers
total_ways_at_least_4_green = ways_scenario_1 + ways_scenario_2

# Probability of selecting at least 4 green peppers
probability = total_ways_at_least_4_green / total_ways

# Simplifying the fraction
numerator = total_ways_at_least_4_green
denominator = total_ways
gcd_value = gcd(numerator, denominator)
simplified_numerator = numerator // gcd_value
simplified_denominator = denominator // gcd_value

# Final answer
final_answer = (simplified_numerator, simplified_denominator)
final_answer
