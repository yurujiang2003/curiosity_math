from sympy import symbols, Eq, solve, log

x = symbols('x')
equation = Eq(4**x, 8)

# Convert to logarithmic form
solution = solve(equation, x)[0]
final_answer = solution.evalf()
final_answer
