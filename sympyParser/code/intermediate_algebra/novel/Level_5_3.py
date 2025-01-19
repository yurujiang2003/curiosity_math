from sympy import symbols, sqrt, Eq, solve

m = symbols('m')
c = 4
c_expr = 2 * sqrt(1 - 1/m)
equation = Eq(c_expr, c)

solution = solve(equation, m)
valid_solution = [val for val in solution if val != 0 and val != 1]
valid_solution
