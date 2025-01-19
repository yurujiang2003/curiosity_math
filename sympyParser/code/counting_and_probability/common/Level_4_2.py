from sympy import symbols, simplify

n = symbols('n')
f_n = 2**n - (2**n - 1)
min_value = simplify(f_n.subs(n, 2015))

min_value
