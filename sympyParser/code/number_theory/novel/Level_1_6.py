from sympy import symbols, floor

# Define the number of marbles brought by each player
sally_marbles = 239
wei_hwa_marbles = 174
zoe_marbles = 83

# Calculate the total number of marbles
total_marbles = sally_marbles + wei_hwa_marbles + zoe_marbles

# Calculate the number of complete piles of 10 marbles
complete_piles = floor(total_marbles / 10)

# Calculate the total number of marbles used in these complete piles
marbles_in_complete_piles = complete_piles * 10

# Determine how many marbles need to be removed
marbles_to_remove = total_marbles - marbles_in_complete_piles

# Return the final answer
marbles_to_remove
