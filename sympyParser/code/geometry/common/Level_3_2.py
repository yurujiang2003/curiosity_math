from sympy import symbols, Eq, solve

E = 14
n = symbols('n')
edges_eq = Eq(3*n, E)
n_value = solve(edges_eq, n)[0]

V = n_value + 1
V
