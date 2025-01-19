from sympy import binomial

# Define the dimensions of the grid
rows = 6
cols = 6

# Case 1: Rectangles of size 1 x 3
height_choices_case1 = binomial(rows, 2)  # Choosing 2 horizontal lines
width_choices_case1 = cols - 3 + 1  # Possible starting positions for width 3
total_case1 = height_choices_case1 * width_choices_case1

# Case 2: Rectangles of size 3 x 1
height_choices_case2 = rows - 3 + 1  # Possible starting positions for height 3
width_choices_case2 = binomial(cols, 2)  # Choosing 2 vertical lines
total_case2 = height_choices_case2 * width_choices_case2

# Final calculation
total_rectangles = total_case1 + total_case2
total_rectangles
