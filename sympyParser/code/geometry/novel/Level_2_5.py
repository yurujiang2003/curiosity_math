from sympy import symbols, Eq, solve, cbrt

# Define variables
s = symbols('s')

# Original volume of the cube
original_volume = 2**3

# New volume after increasing by 19 cubic centimeters
new_volume = original_volume + 19

# Equation for the volume of the new cube
equation = Eq(s**3, new_volume)

# Solve for s
solution = solve(equation, s)

# Return the final answer
solution[0]
