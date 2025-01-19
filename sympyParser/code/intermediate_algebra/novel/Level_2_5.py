from sympy import symbols, diff, solve, Interval, oo

x = symbols('x')
f = x**3 + 3*x + 5
f_prime = diff(f, x)

# Check if f' is always positive
is_strictly_increasing = all(f_prime.subs(x, val) > 0 for val in [-10, -5, 0, 5])

# Evaluate f at specific points
f_neg2 = f.subs(x, -2)
f_neg1 = f.subs(x, -1)

# Determine the number of real roots
if is_strictly_increasing and f_neg2 < 0 < f_neg1:
    number_of_real_roots = 1
else:
    number_of_real_roots = 0

number_of_real_roots
