from sympy import symbols, Rational

length = 100  # cm
width = 40    # cm
rock_volume = 1000  # cm^3

base_area = length * width
h = rock_volume / base_area

h_rounded = round(float(h), 2)
h_rounded
