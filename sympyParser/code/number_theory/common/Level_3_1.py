from sympy import symbols, mod

# Define the variables
n = 1342
d = 13

# Calculate the remainder r when n is divided by d
r = n % d

# Initialize k
k = 1
while True:
    # Calculate the multiple of n
    multiple = k * n
    # Calculate the remainder of the multiple when divided by d
    remainder = multiple % d
    # Check if the remainder is less than r
    if remainder < r:
        break
    k += 1

# Final answer
result = multiple
result
