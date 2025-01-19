from sympy import symbols, Mul

# Define the number of members
members = 20

# Calculate the number of ways to select the president, vice-president, and treasurer
president_options = members
vice_president_options = members - 1
treasurer_options = members - 2

# Total ways
total_ways = Mul(president_options, vice_president_options, treasurer_options)

total_ways
