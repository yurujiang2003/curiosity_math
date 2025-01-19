from sympy import sqrt, Rational

# Define the distances
d_st_paul_airport = 8
d_minneapolis_airport = 10

# Calculate the distance using the Pythagorean theorem
d_squared = d_st_paul_airport**2 + d_minneapolis_airport**2
distance = sqrt(d_squared)

# Round to the nearest integer
final_distance = round(distance)

final_distance
