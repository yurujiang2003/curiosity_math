from sympy import symbols

# Define variables
width_picture = 5  # inches
height_picture = 7  # inches
border_width = 0.5  # inches

# Calculate total dimensions including the border
total_width = width_picture + 2 * border_width
total_height = height_picture + 2 * border_width

# Calculate areas
area_red_paper = total_width * total_height
area_picture = width_picture * height_picture

# Calculate area of visible red border
area_visible_red_border = area_red_paper - area_picture

area_visible_red_border
