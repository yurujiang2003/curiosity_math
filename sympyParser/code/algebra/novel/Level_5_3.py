from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
eq1 = -x**2 - x + 1
eq2 = 2*x**2 - 1

intersection_eq = Eq(eq1, eq2)
solution = solve(intersection_eq, x)

a = solution[0]
c = solution[1]

c_minus_a = c - a
final_answer = c_minus_a.simplify()

final_answer
