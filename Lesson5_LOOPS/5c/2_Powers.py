in1 = int(input())
in2 = int(input())
in3 = int(input())

for i in range (in1,in2+1):
    lis = []
    for j in range (2, in3+1):
        num = i**j
        lis.append(str(num))
    print(', '.join(lis))

