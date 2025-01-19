from sympy import symbols, summation, sqrt, integrate

n = symbols('n')
S = summation(1 / ((sqrt(n) + sqrt(n + 1)) * (n**(1/4) + (n + 1)**(1/4))), (n, 1, 9999))

N = 9999
integral_approximation = integrate(1 / (n**(3/4)), (n, 1, N))
result = (1/4) * (4 * N**(1/4) - 4)

result.evalf()
