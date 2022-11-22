import math 

iv = int(input())
a = int(input()) 
t = float(input())
g = 9.81

angle = a * (math.pi/180)

x=int(round(iv*math.cos(angle)*t));
y=int(round(iv*math.sin(angle)*t-(g*t**2)/2));
print(f'{x}, {y}')
