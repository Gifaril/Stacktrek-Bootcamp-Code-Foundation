i = float(input())
if i < 2.0:
  print('Micro')
elif i >= 2.0 and i <3:
  print('Very minor')
elif i >= 3.0 and i <4:
  print('Minor')
elif i >= 4.0 and i <5:
  print('Lightr')
elif i >= 5.0 and i <6:
  print('Moderate')
elif i >= 6.0 and i <7:
  print('Strong')
elif i >= 7.0 and i <8:
  print('Major')
elif i >= 9.0 and i <10:
  print('Great')
else:
  print('Meteoric')