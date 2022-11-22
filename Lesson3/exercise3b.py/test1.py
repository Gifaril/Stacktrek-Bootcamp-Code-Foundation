copy = int(input())
price = 24.95
ship = 3
shipping = (copy - 1) *0.75 + ship
discount = price * 0.6
discounted_price= (discount)
total_books = discounted_price * copy
total_bill = total_books + shipping
print(total_bill)

print("Dollars:"+ str(dollars) + "\n"+ "Quarters:" + str(quarters) + "\n"+ "Dimes:"+ str(dimes) + "\n"+ "Nickels:" + str(nickels) + "\n" + "Pennies:" + str(pennies))


import math 
a = int(input())
b = int(input())
print(f"The length of the diagonal is {round(math.sqrt(a**2+b**2), 3)}.")

#area of polygon
from math import tan, pi
s_length = float(input())
n_sides = int(input())

p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print(format(p_area, '.2f'))