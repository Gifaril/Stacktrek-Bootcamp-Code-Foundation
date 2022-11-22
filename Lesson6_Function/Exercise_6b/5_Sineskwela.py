def commoncharacters( w1, w2 ):
  common = []
  for i in w1:
    for j in w2:
      if i == j:
        if (not i in common):
          common.append(i)
  if (len(common) == 1):
    return f'The words have one character in common'
  return f'The words have {len(common)} characters in common'