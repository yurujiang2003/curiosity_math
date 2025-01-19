from sympy import symbols, Poly

x = symbols('x')
numerator = 2*x**7 - 5*x**4 + 3*x**3 - x + 5
degree_numerator = Poly(numerator).degree()

# To have a horizontal asymptote, degree of q(x) must be at least the degree of the numerator
smallest_degree_q = degree_numerator

smallest_degree_q
