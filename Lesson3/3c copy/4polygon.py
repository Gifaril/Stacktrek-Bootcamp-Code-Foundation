from math import tan, pi
s_length = float(input())
n_sides = int(input())

p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print(format(p_area, '.2f'))