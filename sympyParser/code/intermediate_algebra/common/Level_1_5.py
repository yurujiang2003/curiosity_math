from sympy import symbols, Poly

x = symbols('x')
f = Poly(x**4 + 5*x**3 + 9*x**2 - x - 14)

possible_roots = [1, -1, 2, -2, 7, -7, 14, -14]
integer_roots = []

for root in possible_roots:
    if f.eval(root) == 0:
        integer_roots.append(root)

integer_roots
