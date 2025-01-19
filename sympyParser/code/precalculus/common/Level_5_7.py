from sympy import symbols, sqrt, Rational

# Define variables
C1 = (3, -5, 7)
C2 = (0, 1, 1)
r1 = 5 * sqrt(5)
r2 = 2 * sqrt(17)

# Calculate distance d
d = sqrt((C1[0] - C2[0])**2 + (C1[1] - C2[1])**2 + (C1[2] - C2[2])**2)

# Calculate h
r1_squared = r1**2
r2_squared = r2**2
h = (r1_squared - r2_squared + d**2) / (2 * d)

# Calculate R
R_squared = r1_squared - h**2
R = sqrt(R_squared)

R.evalf()
