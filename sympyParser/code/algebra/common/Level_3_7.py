from sympy import symbols, Eq, solve

# Define variables
people_initial = 5
time_initial = 12
time_desired = 3

# Calculate total work in person-hours
total_work = people_initial * time_initial

# Define the variable for the number of people needed
x = symbols('x')

# Set up the equation for the desired time
equation = Eq(x * time_desired, total_work)

# Solve for the number of people needed
people_needed = solve(equation, x)[0]

# Calculate how many more people are needed
more_people_needed = people_needed - people_initial

more_people_needed
