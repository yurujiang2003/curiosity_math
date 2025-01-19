from sympy import symbols, Add, div

# Define the number of marbles each player has
sally_marbles = 239
wei_hwa_marbles = 174
zoe_marbles = 83

# Calculate total marbles
total_marbles = Add(sally_marbles, wei_hwa_marbles, zoe_marbles)

# Calculate the number of complete piles of 10
piles, remainder = div(total_marbles, 10)

# Calculate the number of marbles to be removed
marbles_to_remove = remainder

# Return the final answer
marbles_to_remove
