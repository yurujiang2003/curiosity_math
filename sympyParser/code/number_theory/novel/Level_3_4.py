from sympy import factorial

# Calculate 12!
fact_12 = factorial(12)

# Convert to string to find the digit a
fact_str = str(fact_12)

# Extract the digit a from the string representation
a = fact_str[2]  # The third character corresponds to the digit a

# Return the final answer as an integer
int(a)
