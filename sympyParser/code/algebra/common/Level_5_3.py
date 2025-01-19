from sympy import symbols, Eq, solve, sqrt

x = symbols('x')
equation1 = -x**2 - x + 1
equation2 = 2*x**2 - 1

equation = Eq(equation1, equation2)
rearranged_equation = Eq(-3*x**2 - x + 2, 0)

solutions = solve(rearranged_equation, x)
a = min(solutions)
c = max(solutions)

result = c - a
result.simplify()
