from sympy import symbols, factor, Poly

x = symbols('x')
polynomial = x**12 - 1
factored = factor(polynomial)

irreducible_factors = [Poly(factor, domain='ZZ') for factor in factored.as_ordered_factors()]
k = len(irreducible_factors)

k
