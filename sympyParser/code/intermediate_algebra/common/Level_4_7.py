from sympy import sqrt, Rational

a = Rational(64, 5)
b = Rational(-48, 5)

a_squared = a**2
b_squared = b**2

modulus_z4 = sqrt(a_squared + b_squared)
modulus_z = modulus_z4**(1/4)

result = modulus_z.evalf()
result
