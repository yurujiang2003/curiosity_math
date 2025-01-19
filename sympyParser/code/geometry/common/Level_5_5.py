from sympy import pi, cos, sqrt, N

C = 25100  # circumference of the Earth in miles
R = C / (2 * pi)  # radius of the Earth
latitude = 45  # latitude in degrees

r = R * cos(latitude * pi / 180)  # radius at 45 degrees North Latitude
C_L = 2 * pi * r  # circumference at 45 degrees North Latitude

final_answer = round(N(C_L), -2)  # round to the nearest hundred miles
final_answer
