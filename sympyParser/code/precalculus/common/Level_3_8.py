from sympy import I, sqrt, cos, sin, pi, simplify

# Define the complex number
z = -1 + I * sqrt(3)

# Compute the modulus
r = abs(z)

# Compute the argument
theta = z.as_real_imag()[1] / z.as_real_imag()[0]
theta = pi - pi/3  # Adjust for second quadrant

# Apply De Moivre's Theorem
n = 8
result = r**n * (cos(n * theta) + I * sin(n * theta))

# Simplify the result to rectangular form
final_result = simplify(result)
final_result
