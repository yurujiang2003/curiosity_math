from sympy import Rational

# Define the variables
students_wearing_red_class = 11
total_students_class = 24
total_students_school = 480

# Calculate the ratio of students wearing red
ratio_wearing_red = Rational(students_wearing_red_class, total_students_class)

# Estimate the number of students wearing red in the school
estimated_students_wearing_red = ratio_wearing_red * total_students_school

# Return the final answer
estimated_students_wearing_red.evalf()
