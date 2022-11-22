import os
os.system('cls||clear')

#----CODE STARTS HERE------
from math import sqrt
flag = True
count = 0;
first_x = 0
first_y = 0
temp_x = 0
temp_y  = 0
subtotal = 0
distance = 0
while flag == True:
    x = input()
    if(x == 'stop'):
        subtotal += (temp_x * first_y) - (temp_y * first_x)
        distance += (sqrt((temp_x - first_x)**2 + (temp_y - first_y)**2))
        flag = False
        continue
    else:
        y = int(input())
        if count == 0:
            first_x = int(x)
            first_y = int(y)
            temp_x = int(x)
            temp_y = int(y) 
            count += 1
        else:
            distance += (sqrt((int(x) - temp_x)**2 + (int(y) - temp_y)**2))
            subtotal += (temp_x * int(y)) - (temp_y * int(x))
            temp_x = int(x)
            temp_y = int(y)
            count += 1

print(f"Perimeter: {distance}")
print(f"Area: {abs(subtotal/2)}")

  
    


# distance1 = (math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
# distance2 = (math.sqrt((x3 - x1)**2 + (y3 - y1)**2))
# distance3 = (math.sqrt((x3 - x2)**2 + (y3 - y2)**2))

# distance_final = distance1 + distance2 + distance3
# area = (abs((x1 * y2) - (y1 * x2) + (x2 * y3) - (y2 * x3) + (x3 * y1) - (y3 * x1))/2)

# print("Perimeter:", distance_final)
# print("Area:", area)



