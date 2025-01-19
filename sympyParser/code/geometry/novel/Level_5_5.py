from sympy import pi, sqrt, N

C_equator = 25100  # miles
R = C_equator / (2 * pi)  # radius of the Earth
latitude = 45  # degrees

r = R * (sqrt(2) / 2)  # radius at 45 degrees latitude
C_L = 2 * pi * r  # circumference at 45 degrees latitude

final_answer = round(N(C_L), -2)  # round to the nearest hundred miles
final_answer
