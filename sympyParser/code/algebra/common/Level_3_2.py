from sympy import symbols, Eq, solve

a, b = symbols('a b')
equation = Eq(2*a - 3*b, -23)
b_expr = a + 1
equation_substituted = equation.subs(b, b_expr)

solution = solve(equation_substituted, a)
final_answer = solution[0]
final_answer
