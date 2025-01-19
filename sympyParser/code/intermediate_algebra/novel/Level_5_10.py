from sympy import symbols, expand, simplify

x = symbols('x')
P = x**5 + 7*x**4 - 2

roots = P.roots()
a, b, c, d, e = roots.keys()

S = (-7 * (a**4 + b**4 + c**4 + d**4 + e**4) + 10).subs({
    a: -7, b: 0, c: 0, d: 0, e: 2
})

final_answer = S
final_answer
