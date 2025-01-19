from sympy import sqrt, symbols, simplify, prod

# Define the variable
y = sqrt(2 + sqrt(2 + sqrt(2)))

# Define the function psi recursively
def psi(n):
    if n == 0:
        return 0
    elif n == 1:
        return y
    else:
        return simplify(psi(n-1)**3 - 3*psi(n-1))

# Calculate the product for n from 1 to 100
result = prod(psi(3**n) for n in range(1, 101))

# Return the final answer
result
