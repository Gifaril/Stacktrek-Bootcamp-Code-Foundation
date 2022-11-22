month = input()
days = int(input())
deluxe = 0
premium = 0
month = month.lower()
if (month == 'may' or month == 'october'):
  deluxe = 100 * days
  premium = 85 * days
  if days > 14:
    deluxe = deluxe * 0.70
  elif days > 7:
    deluxe = deluxe * 0.95
elif (month == 'july' or month == 'september'):
  deluxe = 112.50 * days
  premium = 90.58 * days
  if days > 14:
    deluxe = deluxe * 0.80
elif (month == 'june' or month == 'august'):
  deluxe = 125.66 * days
  premium = 100.50 * days

if (days > 14):
  premium = premium * 0.90

print(f'Deluxe: {deluxe:.2f} dollars')
print(f'Premium: {premium:.2f} dollars')