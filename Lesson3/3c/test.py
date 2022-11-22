#1
import math 
a = int(input())
b = int(input())
print(f"The length of the diagonal is {round(math.sqrt(a**2+b**2), 3)}.")

#2

#3
import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = format(math.dist([x1,y1], [x2,y2] ), '.2f')
print(distance)

#4
from math import tan, pi
s_length = float(input())
n_sides = int(input())

p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print(format(p_area, '.2f'))

#5
import math 

iv = int(input())
a = int(input()) 
t = float(input())
g = 9.81

angle = a * (math.pi/180)

x=int(round(iv*math.cos(angle)*t));
y=int(round(iv*math.sin(angle)*t-(g*t**2)/2));
print(f'{x}, {y}')