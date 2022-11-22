target = int(input())
puzzle = int(input()) 
order_p = puzzle* 14
talking_doll = int(input())
order_td = talking_doll* 3
teddy_bear = int(input())
order_tb = teddy_bear* 20.2
pokemon_plushie = int(input())
order_pp = pokemon_plushie* 8.20
big_truck = (int(input())) 
order_bt = big_truck* 10.65

total_order = (puzzle + talking_doll + teddy_bear + pokemon_plushie + big_truck)
total_price = (order_p + order_td + order_tb + order_pp + order_bt)
total_discounted = total_price
if (total_order >=50):
  total_discounted = total_price *0.75
total_rental = total_discounted * 0.90
remaining = total_rental - target
formattedremaining =format(remaining, ".2f")
negative = format(abs(remaining),".2f")
if remaining > 0 :
    print(f"Yes! {formattedremaining} dollars left.")
else:
    print(f"Not enough money! {negative} dollars needed.")