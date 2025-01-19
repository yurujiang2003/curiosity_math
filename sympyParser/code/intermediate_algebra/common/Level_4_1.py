from sympy import symbols, summation, sqrt, Rational, integrate

n = symbols('n')
S = summation(1 / ((sqrt(n) + sqrt(n + 1)) * (n**(1/4) + (n + 1)**(1/4))), (n, 1, 9999))

# Approximate the sum using the integral
x = symbols('x')
integral_approx = integrate(1 / (4 * x**(3/4)), (x, 1, 9999))

final_answer = integral_approx
final_answer
