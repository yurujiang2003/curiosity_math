from sympy import symbols, sqrt, Rational

D = symbols('D', positive=True)
cos_D = Rational(1, 3)
sin_D = sqrt(1 - cos_D**2)

sin_F = cos_D
sin_F_value = sin_F.evalf()
sin_F_value
