from sympy import symbols, Eq, solve

# Define the variables
F, B, G, V_F, V_B, V_G = symbols('F B G V_F V_B V_G')

# Given values and relationships
F_value = 1.00
B_value = F_value + 0.6 * F_value
G_value = B_value - 0.25 * B_value
V_G_expr = (4/3) * V_F
V_B_expr = 0.75 * V_G_expr

# Set up the equations
equation1 = Eq(F, F_value)
equation2 = Eq(B, B_value)
equation3 = Eq(G, G_value)
equation4 = Eq(V_B, V_B_expr)

# Solve for G
solution = solve((equation1, equation2, equation3, equation4), (F, B, G, V_B))
G_cents = solution[G] * 100

G_cents
