from sympy import binomial

n_switches = 8
ways_one_on = binomial(n_switches, 1)
ways_two_on = binomial(n_switches, 2)
total_ways = ways_one_on + ways_two_on

total_ways
