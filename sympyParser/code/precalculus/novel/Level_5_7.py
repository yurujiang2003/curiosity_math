from sympy import sqrt, Rational

# Define the centers and radii of the spheres
C1 = (3, -5, 7)
C2 = (0, 1, 1)
r1 = 5 * sqrt(5)
r2 = 2 * sqrt(17)

# Calculate the distance between the centers
d = sqrt((C1[0] - C2[0])**2 + (C1[1] - C2[1])**2 + (C1[2] - C2[2])**2)

# Calculate r1^2 and r2^2
r1_squared = r1**2
r2_squared = r2**2

# Calculate h
h = (r1_squared - r2_squared + d**2) / (2 * d)

# Calculate the radius of the intersection circle
r = sqrt(r1_squared - h**2)

# Final answer
r.evalf()
