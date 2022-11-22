call = int(input())
text = int(input())

maxText = 100
maxCall = 60
textCharges = 0
callCharges = 0
if (text > maxText):
  textCharges = (text - maxText)
if call > maxCall:
  callCharges = (call - maxCall) * 6.50

total = 799 + textCharges + callCharges + 25

tax = total * 0.05
total_bill = total + tax
call = format(call, '.1f')
text = format(text, '.1f')
callCharges = format(callCharges, '.2f')
textCharges = format(textCharges, '.2f')
tax = format(tax, '.2f')
total_bill = format(total_bill, '.2f')
print(f'Call minutes: {call}')
print(f'Text messages: {text}')
print(f'Excess minute charges: {callCharges}')
print(f'Excess SMS charges: {textCharges}')
print(f'911 fee: 25.00')
print(f'Tax: {tax}')
print(f'Total bill: {total_bill}')