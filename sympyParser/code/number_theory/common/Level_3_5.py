from sympy import div

def convert_to_base_n(num, base):
    remainders = []
    while num > 0:
        num, remainder = div(num, base)
        remainders.append(remainder)
    return ''.join(map(str, remainders[::-1]))

base_10_integer = 340
base = 7
result = convert_to_base_n(base_10_integer, base)
result
