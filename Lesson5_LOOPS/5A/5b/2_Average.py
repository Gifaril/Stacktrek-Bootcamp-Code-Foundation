num = 1
sum1 = 0
length = 0
while num != 0:
    inp = int(input())
    num = inp
    if (inp == 0):
        continue
    sum1 = sum1 + inp
    length = length+ 1
print(abs(sum1/length))