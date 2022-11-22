# in1 =int(input())
count_m = 3
count_f = 4

if count_f == 0:
    print("All males")
elif count_m == 0:
    print("All females")
else:
    small = 0
    if count_m > count_f:
        small = count_f
    else:
        small = count_m
    gcd = 0
    for i in range(1, small + 1):
        if((count_m % i == 0) and (count_f % i == 0)):
            gcd = i
    print(gcd)
    m = int(count_m / gcd)
    f = int(count_f / gcd)
    print(f'{m}:{f}')
    