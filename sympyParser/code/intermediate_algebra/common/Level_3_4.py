from sympy import symbols, degree

x = symbols('x')
numerator = 2*x**7 - 5*x**4 + 3*x**3 - x + 5

degree_numerator = degree(numerator)
smallest_degree_q = degree_numerator  # m = n for horizontal asymptote

smallest_degree_q
