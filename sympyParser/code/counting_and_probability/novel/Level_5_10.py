from sympy import symbols, Function, Matrix

# Define the number of paths to each letter
paths_to_A = 4
paths_from_A_to_T = [12, 12, 14, 14]  # Paths from each A to T
total_paths_A_to_T = sum(paths_from_A_to_T)

# Define paths from T to H
# Assuming symmetry and similar counting, we can define a placeholder for paths from T to H
# For simplicity, let's assume there are 24 paths from each T to H
paths_from_T_to_H = 24  # This is a hypothetical number for demonstration

# Total paths from M to A to T to H
total_paths_M_to_H = paths_to_A * total_paths_A_to_T * paths_from_T_to_H

total_paths_M_to_H
