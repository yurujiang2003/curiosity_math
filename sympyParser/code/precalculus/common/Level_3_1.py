from sympy import symbols, Eq, solve, sqrt

# Define variables
AD, AB, AC, BD, CD = symbols('AD AB AC BD CD')

# Given values
AB_value = 6
AC_value = 3
cos_60 = 1/2

# Law of Cosines equations
eq1 = Eq(AD**2, AB_value**2 + BD**2 - 2 * AB_value * BD * cos_60)
eq2 = Eq(AD**2, AC_value**2 + CD**2 - 2 * AC_value * CD * cos_60)

# Substitute values into equations
eq1 = eq1.subs(AB, AB_value).subs(AC, AC_value)
eq2 = eq2.subs(AC, AC_value)

# Set BD + CD = BC
BC = symbols('BC')
BD_value = symbols('BD_value')
CD_value = BC - BD_value

# Substitute CD in eq2
eq2 = eq2.subs(CD, CD_value)

# Solve for AD
solution = solve((eq1, eq2), (AD, BD_value))
AD_value = sqrt(24)

AD_value
