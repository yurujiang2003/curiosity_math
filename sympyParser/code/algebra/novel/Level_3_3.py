from sympy import symbols, cbrt

x = symbols('x')

def f(x):
    return x**3 - 8

def f_inv(y):
    return cbrt(y + 8)

result = f_inv(f(f_inv(19)))
result
