inp1 = int(input())
inp2 = int(input())
inp3 = int(input())
inp4= int(input())
inp5= int(input())
inp6= int(input())
inp7= int(input())
inp8= int(input())
inp9= int(input())
inp10= int(input())

high= inp1
low = inp1
divi = 0
list1 = [inp1, inp2, inp3,inp4,inp5, inp6,inp7,inp8,inp9,inp10]
for i in list1:
  if i > high:
    high = i
  if i < low:
    low = i
  if i % 3 == 0:
    divi = divi+ 1

print(f'Highest: {high}')
print(f'Lowest: {low}')
print(f'{divi} numbers divisible by 3')
