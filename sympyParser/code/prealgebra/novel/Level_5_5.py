from sympy import symbols

# Define variables
width_picture = 5  # inches
height_picture = 7  # inches
border_width = 0.5  # inches

# Calculate dimensions of the red paper
width_red_paper = width_picture + 2 * border_width
height_red_paper = height_picture + 2 * border_width

# Calculate area of the red paper and the picture
area_red_paper = width_red_paper * height_red_paper
area_picture = width_picture * height_picture

# Calculate area of the visible red border
area_visible_red_border = area_red_paper - area_picture

area_visible_red_border
