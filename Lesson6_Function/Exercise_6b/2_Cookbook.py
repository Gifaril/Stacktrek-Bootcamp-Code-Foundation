def reduce_measure(num, unit):
  if (unit == 'cups'):
    if (num == 1):
      return f'{num} cup'
    return f'{num} cups'
  if (unit == 'tablespoons'):
    if (num == 1):
      return f'{num} tablespoon'
    if ( not num // 16 > 0 ):
      return f'{num} tablespoons'
    cup = int(num // 16)
    tb = num - (cup * 16)
    if (tb == 0):
      if (cup == 1):
        return f'{cup} cup'
      return f'{cup} cups'
    unCup = 'cups'
    unTb = 'tablespoons'
    if (cup == 1):
      unCup = 'cup'
    if (tb == 1):
      unTb = 'tablespoon'
    return f'{cup} {unCup}, {tb} {unTb}'
  if (num < 3):
    if (num == 1):
      return f'{num} teaspoon'
    return f'{num} teaspoons'
  cup = int(int(num / 3) / 16)
  tb = int( (num - (cup * 16 * 3)) / 3)
  ts = int(num - (cup * 16 * 3) - (tb * 3))
  print(ts)
  unCup = 'cups'
  unTb = 'tablespoons'
  unTs = 'teaspoons'
  
  arr = [cup, tb, ts]
  returnStr = ''
  for i in range (len(arr)):
    print(arr[i])
    if (arr[i] <= 0):
      continue
    if (arr[i] ==1):
      if (i == 0):
        unCup = 'cup'
      elif (i == 1):
        unTb = 'tablespoon'
      else:
        unTs = 'teaspoon'
    un = ''
    if (i == 0):
      un = unCup
    elif (i == 1):
      un = unTb
    else:
      un = unTs
    if (len(arr) -1 == i):
      returnStr = returnStr + f'{arr[i]} {un}'
    else:
      returnStr = returnStr + f'{arr[i]} {un}, '
  return returnStr
print(reduce_measure(49, 'tablespoons'))