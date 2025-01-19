from sympy import symbols, factor, Poly

x = symbols('x')
polynomial = x**12 - 1
factored = factor(polynomial)

irreducible_factors = [Poly(f, x).as_expr() for f in factored.as_ordered_factors() if Poly(f, x).is_irreducible]
k = len(irreducible_factors)

k
