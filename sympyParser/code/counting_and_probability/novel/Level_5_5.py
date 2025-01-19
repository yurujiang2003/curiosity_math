from sympy import symbols, binomial

# Define the sets
tina_set = [1, 2, 3, 4, 5]
sergio_set = list(range(1, 11))

# Step 1: Find all possible pairs and their sums
sums = []
pairs = []
for i in range(len(tina_set)):
    for j in range(i + 1, len(tina_set)):
        pair_sum = tina_set[i] + tina_set[j]
        pairs.append((tina_set[i], tina_set[j]))
        sums.append(pair_sum)

# Step 2: List the distinct sums
distinct_sums = set(sums)

# Step 3: Determine the total number of pairs
total_pairs = binomial(len(tina_set), 2)

# Step 4: Determine the possible outcomes for Sergio
total_choices = len(sergio_set)

# Step 5: Calculate the favorable outcomes
favorable_outcomes = 0
for sum_value in distinct_sums:
    count_greater = len([num for num in sergio_set if num > sum_value])
    count_pairs = sums.count(sum_value)
    favorable_outcomes += count_pairs * count_greater

# Step 6: Calculate the total probability
total_outcomes = total_pairs * total_choices
probability = favorable_outcomes / total_outcomes

# Return the final answer
probability
