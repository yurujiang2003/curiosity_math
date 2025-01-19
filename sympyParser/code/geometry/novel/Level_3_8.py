from sympy import symbols, Rational

# Define variables
volume_rock = 1000  # cm^3
length = 100  # cm
width = 40    # cm

# Calculate base area of the aquarium
base_area = length * width  # cm^2

# Calculate rise in water level
h = volume_rock / base_area  # cm

# Return the final answer rounded to the nearest hundredth
final_answer = round(float(h), 2)
final_answer
