dress = int(input())
organizer = int(input())
print(f"{dress*50}{organizer * 125}")

inp = int(input())
tray = (inp // 12) * 70
peices = (inp % 12) * 7
print(tray + peices)

p = int(input())
r = int(input())
n = int(input())
print(format(p*(1 + (r*0.01))**n, ".2f"))

inp = int(input())
tax = inp * 0.12
withoutTax = inp - tax
tip = withoutTax * 0.10
print('Tax: '+ str(format(tax, ".2f")) + '\n' + 'Emergency Fund: '+str(format(tip, ".2f"))+ '\nAccommodation: ' + str(format(withoutTax-tip,".2f")))
# print('Emergency Fund:'+str(format(tip, ".2f")))
# print('Accommodation:'+str(format(withoutTax-tip,".2f")))