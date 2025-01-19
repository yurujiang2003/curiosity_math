from sympy import I, re, symbols

z = symbols('z')

def f(z):
    if re(z) == z:  # Check if z is real
        return z + 2
    else:
        return z**2

result = f(I) + f(1) + f(-1) + f(-I)
result
