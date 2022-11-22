a = int(input())
b = int(input())
c = int(input())

if (a > 50 and a < 1) and (b > 50 and b < 1) and (c > 50 and c < 1):
  print("Please enter numbers between 1 and 50")
else:
  sec = a + b +c
  min = sec // 60
  sec -= (min * 60)
  print(f"{min}:{sec:02d}")

