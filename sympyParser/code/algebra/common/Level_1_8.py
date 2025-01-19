from sympy import symbols, Function

x = symbols('x')
f = Function('f')(x)
g = Function('g')(x)

f = 2*x + 1
g = -3

result = f.subs(x, g)
result
