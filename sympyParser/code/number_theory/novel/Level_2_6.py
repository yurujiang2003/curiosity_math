from sympy import symbols, Add, div

# Define the amounts earned in dollars
linda = 27.47
sherry = 35.23
june = 37.37
connie = 26.52

# Convert dollars to cents
linda_cents = linda * 100
sherry_cents = sherry * 100
june_cents = june * 100
connie_cents = connie * 100

# Calculate the total amount in cents
total_cents = Add(linda_cents, sherry_cents, june_cents, connie_cents)

# Convert total cents to dollars and determine the remainder
dollars, remainder = div(total_cents, 100)

# Return the final answer
remainder
