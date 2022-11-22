inp = int(input())
dollar = 100
q = 25
d= 10
n = 5
p = 1
dollars = int(inp / dollar)
quarters = int((inp - (dollars * dollar)) // q )
dimes = int((inp - (dollars * dollar) - (quarters * q)) // d )
nickels = int((inp - (dollars * dollar) - (quarters * q) - (dimes * d)) // n )
pennies = int((inp - (dollars * dollar) - (quarters * q) - (dimes * d) - (nickels * n)) // p )
print(str(inp / dollar)+" consists of:\nDollars: "+ str(dollars) + "\n"+ "Quarters: " + str(quarters) + "\n"+ "Dimes: "+ str(dimes) + "\n"+ "Nickels: " + str(nickels) + "\n" + "Pennies: " + str(pennies))


#11 1156 // 100
#2 1156- 1100 // 25
# print(int((inp - (dollars * dollar) - (quarters * q) - (dimes * d) - (nickels * n)) ))
# print(inp - (dollars * dollar))
# print(inp - (dollars * dollar) - (quarters * q))
# print(inp - (dollars * dollar) - (quarters * q) - (dimes * d))
# print(inp - (dollars * dollar) - (quarters * q) - (dimes * d) - (nickels * n))
# print((inp - (dollars * dollar)))
