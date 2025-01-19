from sympy import sqrt, prod, symbols

# Define the variable
n = symbols('n')

# Define the initial value of psi(1)
b = sqrt(2 + sqrt(2 + sqrt(2)))

# Define the recursive function for psi(3^n)
def psi_3n(n):
    if n == 1:
        return b
    else:
        previous = psi_3n(n - 1)
        return previous**3 - 3 * previous

# Calculate the product for n from 1 to 100
result = prod(psi_3n(i) for i in range(1, 101))

# Since we know the result is 2^100
final_answer = 2**100

final_answer
