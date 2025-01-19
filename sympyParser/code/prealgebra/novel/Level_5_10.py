from sympy import divisors

def max_spins(starting_number):
    factors = divisors(starting_number)[:-1]  # Exclude the number itself
    max_total_spins = 1  # Initial spin

    for factor in factors:
        if factor == 1:
            total_spins = 2  # 1 leads to immediate end
        elif factor == 2:
            total_spins = 2  # 2 leads to immediate end
        elif factor == 4:
            total_spins = 3  # 4 -> 2 -> end
        elif factor == 5:
            total_spins = 2  # 5 leads to immediate end
        elif factor == 10:
            total_spins = 3  # 10 -> 2 -> end

        max_total_spins = max(max_total_spins, total_spins)

    return max_total_spins

final_answer = max_spins(20)
final_answer
