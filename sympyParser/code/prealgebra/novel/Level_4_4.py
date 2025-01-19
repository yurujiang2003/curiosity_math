from sympy import symbols, Mul, Add

# Define costs per square yard
cost_carpet_per_sqyd = 21.95
cost_padding_per_sqyd = 2.55

# Define dimensions and areas
width_large = 4
height_large = 5
area_large = Mul(width_large, height_large)

width_small = 5
height_small = 2
area_small = Mul(width_small, height_small)

# Calculate total area
total_area = area_large - area_small

# Calculate costs
cost_carpet = Mul(total_area, cost_carpet_per_sqyd)
cost_padding = Mul(total_area, cost_padding_per_sqyd)

# Calculate total cost
total_cost = Add(cost_carpet, cost_padding)

total_cost.evalf()
