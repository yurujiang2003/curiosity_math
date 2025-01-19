from sympy import symbols, Eq, solve

# Step 1: Calculate total work in person-hours
people_initial = 5
time_initial = 12
total_work = people_initial * time_initial

# Step 2: Determine how many people are needed to complete the work in 3 hours
x = symbols('x')
time_new = 3
equation = Eq(x * time_new, total_work)

# Solve for x
people_needed = solve(equation, x)[0]

# Step 3: Calculate how many more people are needed
additional_people_needed = people_needed - people_initial

additional_people_needed
