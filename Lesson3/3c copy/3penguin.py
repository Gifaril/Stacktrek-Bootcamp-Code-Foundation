import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

distance = format(math.dist([x1,y1], [x2,y2] ), '.2f')
print(distance)