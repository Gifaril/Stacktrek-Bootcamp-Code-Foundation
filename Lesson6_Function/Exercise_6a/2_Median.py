def median(a,b,c):
  arr = [a, b, c]
  arr.sort()
  return arr[1]

def alternate_median(a,b,c):
  arr = [a, b, c].sort()
  return (arr[1] + arr[2]) / 2

def printx(a,b,c):
   return median(a,b, c)
  # alternate_median(a,b,c)

print(printx(4, 5, 6))