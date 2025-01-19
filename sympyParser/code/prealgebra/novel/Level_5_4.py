from sympy import symbols, Rational

N = symbols('N')

# Step 1: Determine the number of students in each group
group_A_students = 0.8 * N
group_B_students = 0.2 * N

# Step 2: Determine the amount of candy each group shares
candy_A = 0.4
candy_B = 0.6

# Step 3: Calculate the amount of candy per student in each group
candy_per_student_A = candy_A / group_A_students
candy_per_student_B = candy_B / group_B_students

# Step 4: Find the ratio of the amount of candy per student in Group A to Group B
ratio = candy_per_student_A / candy_per_student_B

# Simplifying the ratio to a common fraction
final_ratio = Rational(ratio).simplify()
final_ratio
