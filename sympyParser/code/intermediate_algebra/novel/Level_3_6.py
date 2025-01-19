from sympy import symbols, divisors

x = symbols('x')
constant_term = 1
leading_coefficient = 2

factors_constant = divisors(constant_term)
factors_leading = divisors(leading_coefficient)

possible_rational_roots = set()

for p in factors_constant:
    for q in factors_leading:
        possible_rational_roots.add(p / q)
        possible_rational_roots.add(-p / q)

distinct_rational_roots_count = len(possible_rational_roots)
distinct_rational_roots_count
