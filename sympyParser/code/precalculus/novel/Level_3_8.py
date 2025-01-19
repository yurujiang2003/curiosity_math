from sympy import I, sqrt, cos, sin, pi, simplify

# Define the complex number
z = -1 + I * sqrt(3)

# Compute the modulus
r = abs(z)

# Compute the argument
theta = z.as_real_imag()[1] / z.as_real_imag()[0]

# Convert to polar form
polar_form = r * (cos(2 * pi / 3) + I * sin(2 * pi / 3))

# Apply De Moivre's theorem
result = (polar_form ** 8).expand()

# Simplify the result
final_result = simplify(result)

final_result
