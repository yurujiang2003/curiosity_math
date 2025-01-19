from sympy import symbols, Poly

x = symbols('x')
polynomial = Poly(x**3 - 3*x - 5)
r = polynomial.coeffs()[-1]
abc = -r
abc
