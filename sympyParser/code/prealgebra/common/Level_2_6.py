from sympy import gcd, Rational

numerator = 91
denominator = 26

common_divisor = gcd(numerator, denominator)
simplified_numerator = numerator // common_divisor
simplified_denominator = denominator // common_divisor

result = Rational(simplified_numerator, simplified_denominator)
result
