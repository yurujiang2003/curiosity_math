from sympy import symbols, Rational

C, N = symbols('C N')
group_A_candy = 0.4 * C
group_B_candy = 0.6 * C

students_A = 0.8 * N
students_B = 0.2 * N

candy_per_student_A = group_A_candy / students_A
candy_per_student_B = group_B_candy / students_B

ratio = candy_per_student_A / candy_per_student_B
final_ratio = ratio.simplify()

final_ratio
