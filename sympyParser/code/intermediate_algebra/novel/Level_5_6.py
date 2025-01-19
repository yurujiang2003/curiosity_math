from sympy import symbols, exp, I, Abs

theta, phi, psi = symbols('theta phi psi')
z1 = exp(I * theta)
z2 = 2 * exp(I * phi)
z3 = 3 * exp(I * psi)

# Calculate |z1 + z2 + z3|
result = Abs(z1 + z2 + z3).subs({theta: 0, phi: 0, psi: 0})
result
