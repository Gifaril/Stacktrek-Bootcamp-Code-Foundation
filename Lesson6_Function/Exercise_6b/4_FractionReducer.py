def gcd(n,m):
  d = min(n, m)
  while n % d !=0 or m % d != 0:
    d = d - 1
  return d

def reduce(num, den):
  g = gcd(num, den)
  if num == 0:
    return '0/1'
  x = num // g
  y = den // g
  return  f'{x}/{y}'
   

def display(num, den):
  return f'{num}/{den} can be reduced to {reduce(num, den)}.'
