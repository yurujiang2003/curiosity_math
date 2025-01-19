from sympy import symbols

# Define variables
F, S, B, total_students = 8, 12, 3, 30

# Calculate total taking at least one language
total_at_least_one = F + S - B

# Calculate students taking neither language
students_neither = total_students - total_at_least_one

students_neither
