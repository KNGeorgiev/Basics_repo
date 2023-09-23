import math

ppl_number = int(input())
entry_tax = float(input())
chaiselongue_price = float(input())
umbrella_price = float(input())

umbrella_number = math.ceil(ppl_number / 2)
chaiselongue_number = math.ceil(ppl_number * 0.75)

total_cost = (entry_tax * ppl_number) + (umbrella_price * umbrella_number) +(chaiselongue_price * chaiselongue_number)

print(f"{total_cost:.2f} lv.")
