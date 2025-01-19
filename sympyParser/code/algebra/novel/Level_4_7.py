from sympy import I, re

def f(z):
    if re(z) == z:  # z is real
        return z + 2
    else:  # z is not real
        return z**2

result = f(I) + f(1) + f(-1) + f(-I)
result
