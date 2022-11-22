number = int(input("Enter a number:"))
flag = False
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            flag = True
            break
if flag:
    print("Not Prime ")
else:
    print("Prime")
