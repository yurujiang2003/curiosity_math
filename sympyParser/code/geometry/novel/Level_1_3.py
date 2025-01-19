from sympy import symbols

# Define the number of edges in a hexagonal base and the number of bases
edges_per_base = 6
number_of_bases = 2

# Calculate total edges from bases
total_edges_bases = edges_per_base * number_of_bases

# Define the number of vertical edges
vertical_edges = edges_per_base

# Calculate total edges in the hexagonal prism
total_edges = total_edges_bases + vertical_edges

# Return the final answer
total_edges
