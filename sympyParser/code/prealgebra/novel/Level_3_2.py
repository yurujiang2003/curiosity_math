from sympy import symbols

# Variable definitions
F = 8  # Students taking French
S = 12  # Students taking Spanish
B = 3  # Students taking both languages
total_students = 30  # Total number of students

# Calculate the number of students taking at least one language
at_least_one_language = F + S - B

# Calculate the number of students taking neither language
neither_language = total_students - at_least_one_language

# Return the final answer
neither_language
