from sympy import symbols, Eq, simplify, collect, solve, Poly

x = symbols('x')
lhs = (1 / ((7 - x) * (1 + x) * (1 - x))) + (3 * x**2 - 18 * x - 22) / ((x - 1) * (x + 1) * (x - 7)) + (3 / (x - 2))
rhs = 3 / ((x - 1) * (x - 2))

equation = Eq(lhs, rhs)

common_denominator = (7 - x) * (1 + x) * (1 - x) * (x - 1) * (x + 1) * (x - 7) * (x - 2)
equation_multiplied = Eq(equation.lhs * common_denominator, equation.rhs * common_denominator)

polynomial = simplify(equation_multiplied.lhs - equation_multiplied.rhs)
polynomial = collect(polynomial, x)

roots = solve(polynomial, x)
valid_solutions = [r for r in roots if r not in [2, 1, 7, -1]]

number_of_solutions = len(valid_solutions)
number_of_solutions
