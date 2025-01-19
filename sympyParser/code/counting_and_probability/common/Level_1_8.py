from sympy import Rational

# Define the total number of students
total_students = 28

# Calculate the number of students with brown hair and right-handed students
brown_hair_students = Rational(3, 4) * total_students
right_handed_students = Rational(6, 7) * total_students

# Use the inclusion-exclusion principle to find the minimum number of students with both characteristics
min_both = brown_hair_students + right_handed_students - total_students

# Return the final answer
min_both.evalf()
