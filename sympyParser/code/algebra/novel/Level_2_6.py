from sympy import symbols, Eq, solve, log

x = symbols('x')
equation = Eq(4**x, 8)

# Rewrite in terms of powers of 2
equation = Eq((2**2)**x, 2**3)

# Simplify and solve for x
equation = Eq(2**(2*x), 2**3)
solution = solve(equation, x)[0]

solution
