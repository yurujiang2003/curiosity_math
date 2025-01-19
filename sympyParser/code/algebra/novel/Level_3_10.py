from sympy import symbols, Eq, solve, Abs

x = symbols('x')
equation = Eq(x**2, -Abs(x))
solutions = solve(equation, x)
number_of_solutions = len(solutions)

number_of_solutions
