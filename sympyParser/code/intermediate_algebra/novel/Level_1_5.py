from sympy import symbols, Poly

x = symbols('x')
polynomial = Poly(x**4 + 5*x**3 + 9*x**2 - x - 14)

# Possible integer roots based on factors of -14
possible_roots = [1, -1, 2, -2, 7, -7, 14, -14]
integer_roots = []

for root in possible_roots:
    if polynomial.eval(root) == 0:
        integer_roots.append(root)

integer_roots
