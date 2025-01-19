from sympy import symbols, simplify

s = symbols('s')
expression = 4*s**2 + 28*s + 45

# Completing the square
factored_expr = 4 * (s**2 + 7*s)
completed_square = (s + 7/2)**2 - (49/4)
final_expr = simplify(factored_expr.subs(s**2 + 7*s, completed_square))

# Combine with the constant term
final_expr = final_expr + 45
final_expr = simplify(final_expr)

# Extract q
q = final_expr.as_poly().coeffs()[-1]
q
