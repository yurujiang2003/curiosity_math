from sympy import divisors

# Define the numbers
num1 = 80
num2 = 8

# Get the divisors
divisors_of_80 = set(divisors(num1))
divisors_of_8 = set(divisors(num2))

# Find divisors of 80 that are not divisors of 8
valid_m_values = divisors_of_80 - divisors_of_8

# Count the number of valid m values
result = len(valid_m_values)
result
