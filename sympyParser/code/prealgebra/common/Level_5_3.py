from sympy import sqrt, factorint

# Define the numbers
num1 = 56
num2 = 126

# Calculate the product
product = num1 * num2

# Factor the product
factors = factorint(product)

# Calculate the square root of the product
sqrt_product = sqrt(product)

# Calculate a and b
a = 1
b = 1
for prime, exp in factors.items():
    a *= prime ** (exp // 2)
    if exp % 2 != 0:
        b *= prime

# Calculate a + b
result = a + b
result
