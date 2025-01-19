from sympy import symbols

x = symbols('x')

def f(x):
    return x**2 - 3

def t(x):
    return 9 + 2*f(x)

result = t(f(-2))
result
