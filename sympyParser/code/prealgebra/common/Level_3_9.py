from sympy import symbols, factorint

# Define the product
product = 1000

# Factor the product
factors = factorint(product)

# Generate pairs of factors
pairs = []
for i in range(1, int(product**0.5) + 1):
    if product % i == 0:
        pairs.append((i, product // i))

# Filter out pairs where either number is a multiple of 10
valid_pairs = [(a, b) for a, b in pairs if a % 10 != 0 and b % 10 != 0]

# Calculate sums of valid pairs
sums = [a + b for a, b in valid_pairs]

# Get the possible sums
possible_sums = set(sums)

# Return the smallest sum
final_answer = min(possible_sums)
final_answer
