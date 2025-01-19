from sympy import floor, oo, Symbol

x = Symbol('x')

def f(x):
    return floor((-5/8)**x)

distinct_values = set()

for i in range(0, 10):  # Check a range of x values
    distinct_values.add(f(i))

distinct_values_count = len(distinct_values)
distinct_values_count
