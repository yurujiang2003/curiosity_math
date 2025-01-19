from sympy import symbols, Eq, solve, sum

n = symbols('n')
# Set up the equation for the sum of four consecutive integers
equation = Eq(n + (n + 1) + (n + 2) + (n + 3), 22)
# Solve for n
n_value = solve(equation, n)[0]

# Define the four consecutive integers
integers = [n_value + i for i in range(4)]
# Increase each integer by 2
new_integers = [x + 2 for x in integers]
# Multiply each integer by 20
multiplied_integers = [x * 20 for x in new_integers]
# Calculate the sum of the new set of integers
result = sum(multiplied_integers)

result
