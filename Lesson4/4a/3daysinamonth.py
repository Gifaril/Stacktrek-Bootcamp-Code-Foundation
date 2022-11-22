m = int(input())
if m==2:
  print("28 or 29 days")
elif (m % 2 == 0 and m <= 6) or (m % 2 == 1 and m >7):
  print("30 days")
elif (m % 2 == 1 and m <= 7) or (m % 2 == 0 and m >6):
  print("31 days")
else:
  print("Invalid please tyr again")
