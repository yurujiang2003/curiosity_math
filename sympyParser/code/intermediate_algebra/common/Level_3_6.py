from sympy import symbols, divisors

x = symbols('x')
constant_term = 1
leading_coefficient = 2

factors_constant = divisors(constant_term)
factors_leading = divisors(leading_coefficient)

possible_roots = set()
for p in factors_constant:
    for q in factors_leading:
        possible_roots.add(p / q)
        possible_roots.add(-p / q)

distinct_possible_roots = len(possible_roots)
distinct_possible_roots
