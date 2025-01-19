from sympy import symbols

# Define the dimensions of the grid
width = 6
height = 6

# Calculate the number of 1x3 rectangles
width_1 = 1
height_1 = 3
count_1x3 = (width - width_1) * (height - height_1 + 1)

# Calculate the number of 3x1 rectangles
width_2 = 3
height_2 = 1
count_3x1 = (width - width_2 + 1) * (height - height_2)

# Total rectangles of area 3
total_rectangles = count_1x3 + count_3x1
total_rectangles
