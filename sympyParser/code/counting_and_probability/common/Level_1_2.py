from sympy import symbols, Eq, solve

P = 5
M = 8
total_slices = 12
B = symbols('B')

equation = Eq(P + M - B, total_slices)
solution = solve(equation, B)

solution[0]
