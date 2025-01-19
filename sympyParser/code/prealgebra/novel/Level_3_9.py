from sympy import symbols, factorint

# Define the product
product = 1000

# Factor the product
factors = factorint(product)

# Generate pairs of factors
valid_pairs = []
for i in range(1, int(product**0.5) + 1):
    if product % i == 0:
        j = product // i
        if i % 10 != 0 and j % 10 != 0:
            valid_pairs.append((i, j))

# Calculate sums of valid pairs
sums = [x + y for x, y in valid_pairs]

# Return the maximum sum
final_answer = max(sums)
final_answer
