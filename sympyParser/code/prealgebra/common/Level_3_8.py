from sympy import *

# Define the number of students in 2005 for each county
students_2005 = [136, 11, 29, 524, 11, 19, 29, 41]

# Sort the list to find the median
sorted_students = sorted(students_2005)

# Calculate the median
n = len(sorted_students)
if n % 2 == 0:
    median = (sorted_students[n//2 - 1] + sorted_students[n//2]) / 2
else:
    median = sorted_students[n//2]

# Return the final answer
median
