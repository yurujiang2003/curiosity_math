from sympy import symbols, Eq, solve

# Define variables
F, B, G, V_F, V_B, V_G = symbols('F B G V_F V_B V_G')

# Given information
F_value = 100  # Fresh costs $1.00 per unit of volume

# Relationships
B_expr = 1.6 * F  # Bright is 60% more expensive than Fresh
G_expr = 0.75 * B  # Glow is 25% less expensive than Bright
V_G_expr = (4/3) * V_F  # Glow has 33 1/3% more volume than Fresh
V_B_expr = 0.75 * V_G  # Bright has 25% less volume than Glow

# Substitute F_value into B and G
B_value = B_expr.subs(F, F_value)
G_value = G_expr.subs(B, B_value)

# Solve for volumes
V_B_value = V_F  # Since V_B = V_F
V_G_value = V_G_expr.subs(V_F, V_B_value)

# Final answer for Glow's price per unit of volume
final_answer = G_value.evalf()
final_answer
