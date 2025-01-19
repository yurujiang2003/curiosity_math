from sympy import symbols, Eq, solve

a = symbols('a')
x = a + 1
y = 6 * a
z = 6 * a + 1

equation = Eq(x**2 + y**2, z**2)
solution = solve(equation, a)
final_answer = [sol for sol in solution if sol > 0][0]
final_answer
