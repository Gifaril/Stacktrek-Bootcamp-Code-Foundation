def checkPassword(password):
  if (len(password) < 8):
    return False
  numbers = "0123456789"
  upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lower_case = "abcdefghijklmnopqrstuvwxyz"
  up = 0
  num = 0
  low = 0
  for i in range(len(password) -1):
    if password[i] in numbers:
      num = num + 1
    elif password [i] in upper_case:
      up = up + 1
    elif password [i] in lower_case:
      low = low + 1
  if (up == 0 or num==0 or low == 0):
    return False
  return True
  
def display(password):
  if (checkPassword(password)):
    return 'That\'s a good password'
  return 'That isn\'t a good password'
  