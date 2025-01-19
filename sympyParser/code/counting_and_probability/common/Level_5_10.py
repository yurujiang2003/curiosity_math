from sympy import *

# Define the number of paths for each segment
paths_M_to_A = 4
paths_A_to_T = 8
paths_T_to_H = 12

# Calculate the total number of distinct paths
total_paths = paths_M_to_A * paths_A_to_T * paths_T_to_H
total_paths
