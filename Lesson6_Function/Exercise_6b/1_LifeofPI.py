def gregoryLeibnitz( num ):
  pi = 0
  denom = 1
  for i in range(num):
    if i % 2 == 0:
      pi += 4 / denom
      denom += 2
    else:
      pi -= 4/denom
      denom += 2
  return pi
    