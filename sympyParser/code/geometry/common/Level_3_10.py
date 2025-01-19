from sympy import symbols

# Define the coordinates of the squares
squares_colored = {(1, 0), (0, 3), (2, 3), (3, 1)}
symmetric_pairs = {
    (1, 0): (0, 1),
    (0, 3): (3, 0),
    (2, 3): (3, 2),
    (3, 1): (1, 3)
}

# Initialize a set to track additional squares that need to be colored
additional_squares = set()

# Check for each colored square if its symmetric pair is colored
for square in squares_colored:
    symmetric_square = symmetric_pairs[square]
    if symmetric_square not in squares_colored:
        additional_squares.add(symmetric_square)

# Calculate the total number of squares that need to be colored
total_to_color = len(additional_squares)

# Return the final answer
total_to_color
