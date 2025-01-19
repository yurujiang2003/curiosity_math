from sympy import symbols, diff, oo, S

x = symbols('x')
f = x**3 + 3*x + 5
f_prime = diff(f, x)

# Check if the derivative is always positive
is_strictly_increasing = all(f_prime.subs(x, val) > 0 for val in [S.Reals])

# Behavior at the endpoints
f_neg_inf = f.subs(x, -oo)
f_pos_inf = f.subs(x, oo)

# Determine the number of real roots
if is_strictly_increasing and f_neg_inf < 0 and f_pos_inf > 0:
    num_real_roots = 1
else:
    num_real_roots = 0

num_real_roots
