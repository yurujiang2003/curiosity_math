from sympy import symbols, simplify

n = symbols('n')
f_n = 2**n - (2**n - 1)
f_n_simplified = simplify(f_n)

min_value = f_n_simplified.subs(n, 2015)  # Since f(n) is constant, we can substitute any n >= 2015
min_value
