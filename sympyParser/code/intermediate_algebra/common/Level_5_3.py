from sympy import symbols, sqrt, Eq, solve

m = symbols('m')
c_squared = 16
c_expression = 4 * (m - 1) / m

equation = Eq(c_expression, c_squared)
solution = solve(equation, m)
valid_solution = [val for val in solution if val != 0 and val != 1]

valid_solution
