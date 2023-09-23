drink = input()
sugar = input()
drink_number = int(input())
total_cost = 0

if drink == "Espresso":
    if sugar == "Without":
        total_cost = drink_number * 0.90
    if sugar == "Normal":
        total_cost = drink_number * 1
    if sugar == "Extra":
        total_cost = drink_number * 1.20

if drink == "Cappuccino":
    if sugar == "Without":
        total_cost = drink_number * 1
    if sugar == "Normal":
        total_cost = drink_number * 1.20
    if sugar == "Extra":
        total_cost = drink_number * 1.60

if drink == "Tea":
    if sugar == "Without":
        total_cost = drink_number * 0.50
    if sugar == "Normal":
        total_cost = drink_number * 0.60
    if sugar == "Extra":
        total_cost = drink_number * 0.70

if sugar == "Without":
    total_cost = total_cost - total_cost * 0.35

if drink == "Espresso" and drink_number >= 5:
    total_cost = total_cost - total_cost * 0.25

if total_cost > 15:
    total_cost = total_cost - total_cost * 0.20

print(f"You bought {drink_number} cups of {drink} for {total_cost:.2f} lv.")