from sympy import factorial

# Calculate 12!
result = factorial(12)

# Convert result to string to find the digit 'a'
result_str = str(result)

# Extract the digit 'a' from the string representation
a = result_str[2]  # The third character corresponds to 'a'

# Convert 'a' to an integer
a_value = int(a)

# Return the final answer
a_value
