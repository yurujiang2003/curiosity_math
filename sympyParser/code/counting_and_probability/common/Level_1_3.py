from sympy import sqrt, floor, ceil

lower_bound = 200
upper_bound = 300

smallest_n = ceil(sqrt(lower_bound))
largest_n = floor(sqrt(upper_bound))

perfect_squares = [n**2 for n in range(smallest_n, largest_n + 1)]
count_perfect_squares = len(perfect_squares)

count_perfect_squares
