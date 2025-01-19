from sympy import Matrix

# Define the grid size
grid_size = 4

# Define the initial black squares based on the problem statement
initial_black_squares = {(1, 0), (0, 3), (2, 3), (3, 1)}

# Define the pairs that must match for symmetry
pairs = [((0, 1), (1, 0)), ((0, 2), (2, 0)), ((0, 3), (3, 0)),
         ((1, 2), (2, 1)), ((1, 3), (3, 1)), ((2, 3), (3, 2))]

# Count the number of pairs that are not satisfied
additional_black_needed = 0

for (a, b), (c, d) in pairs:
    if (a, b) in initial_black_squares and (c, d) not in initial_black_squares:
        additional_black_needed += 1
    elif (c, d) in initial_black_squares and (a, b) not in initial_black_squares:
        additional_black_needed += 1

# Total black squares needed to achieve symmetry
total_black_needed = len(initial_black_squares) + additional_black_needed

total_black_needed
