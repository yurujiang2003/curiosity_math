from sympy import symbols, Poly

x = symbols('x')
polynomial = Poly(x**3 - 3*x - 5)
r = polynomial.coeff_monomial(x**0)  # constant term
abc = -r
abc
