from sympy import symbols

# Define variables
left_length = 4  # yards
left_width = 3   # yards
bottom_length = 5 # yards
bottom_width = 2  # yards
top_length = 4    # yards
top_width = 2     # yards
carpet_cost_per_sqyd = 21.95  # dollars
padding_cost_per_sqyd = 2.55   # dollars

# Calculate areas
area_left = left_length * left_width
area_bottom = bottom_length * bottom_width
area_top = top_length * top_width
area_right = area_bottom + area_top
total_area = area_left + area_right

# Calculate costs
cost_carpet = total_area * carpet_cost_per_sqyd
cost_padding = total_area * padding_cost_per_sqyd
total_cost = cost_carpet + cost_padding

# Return final answer
total_cost
