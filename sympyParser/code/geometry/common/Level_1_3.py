from sympy import symbols, Add

# Define variables
edges_per_hexagon = 6
number_of_hexagons = 2
lateral_edges = 6

# Calculate total edges
base_edges = edges_per_hexagon * number_of_hexagons
total_edges = Add(base_edges, lateral_edges)

# Return the final answer
total_edges
