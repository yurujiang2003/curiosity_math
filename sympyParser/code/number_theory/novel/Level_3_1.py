from sympy import symbols, div

# Define the numbers
a = 1342
d = 13

# Calculate the remainder r when 1342 is divided by 13
_, r = div(a, d)

# Initialize k
k = 1
n = k * a

# Find the smallest k such that n mod 13 < r
while n % d >= r:
    k += 1
    n = k * a

# Return the final answer
n
