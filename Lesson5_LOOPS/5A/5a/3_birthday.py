age = int(input())
washing = float(input())
toys_income = float(input())
dollar = 0 
even_dollar = 10

for age in range (1, age+1):
    if age % 2 == 0:
        dollar = dollar + even_dollar
        dollar = dollar -1
        even_dollar= even_dollar + 10
    else:
        dollar = dollar + toys_income

total = abs(dollar-washing)
if (dollar >= washing):
    print(f'Yes! you still have {total:.2f} left')
else:
    print(f'No! you still need {total:.2f}')



   




