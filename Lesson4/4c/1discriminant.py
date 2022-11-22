import math
a = float(input())
b = float(input())
c = float(input())

discri =(b**2) - (4*a*c)

if a == 0 and b == 0:
    print('There is not even an unknown in this equation!')
elif discri < 0:
    print('There are no solutions')
elif discri > 0:
    sol1 = (-b + math.sqrt(abs(discri)))/(2 * a)
    sol2 = (-b - math.sqrt(abs(discri)))/(2 * a)
    print(f'There are two solutions , namely {sol1} and {sol2}')
elif discri == 0:
    sol1 = (-b + math.sqrt(abs(discri)))/(2 * a)
    print(f'There is one solution , namely {sol1}')