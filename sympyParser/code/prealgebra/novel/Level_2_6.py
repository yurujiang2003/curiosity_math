from sympy import gcd, Rational

numerator = 91
denominator = 26

gcd_value = gcd(numerator, denominator)
simplified_numerator = numerator // gcd_value
simplified_denominator = denominator // gcd_value

simplified_fraction = Rational(simplified_numerator, simplified_denominator)
simplified_fraction
