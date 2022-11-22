end=False
total= 0
while end == False:
  inp=input()
  if (inp == 'end'):
    end = True
    break
  
  age = int(inp)
  if age<=2:
    continue
  elif age >=3 and age <=12:
    total = total + 14
  elif age >= 65:
    total = total + 18
  else:
    total = total + 23

print(format(total, '.2f'))