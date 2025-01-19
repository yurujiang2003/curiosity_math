from sympy import symbols, solve

N = 28
A = 3/4 * N
B = 6/7 * N

intersection = symbols('intersection')
inequality = A + B - intersection <= N

solution = solve(inequality, intersection)
min_students_both = solution[0]

min_students_both
