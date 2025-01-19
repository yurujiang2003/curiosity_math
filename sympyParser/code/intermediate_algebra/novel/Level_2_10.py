from sympy import symbols, factor, Rational

x = symbols('x')
polynomial = x**3 - 9*x**2 + 27*x - 35

# Factor the polynomial
factored_polynomial = factor(polynomial)
factored_polynomial
