from sympy import symbols, Sum, simplify

n = 100
x = symbols('x')
expression = Sum((-1)**(n - i) * i, (i, 1, n))
result = simplify(expression.doit())
result
