# Предприемчив българин отваря квартални магазинчета в няколко града и продава на различни цени според града:
# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	            0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna	            0.45	0.70	1.10	1.35	1.55
# Напишете програма, която чете продукт (текст), град (текст) и количество (десетично число),
# въведени от потребителя, и пресмята и отпечатва колко струва съответното количество от избрания продукт в посочения град.

product = str(input())
town = str(input())
qty = float(input())

if town == "Sofia":
    if product == "coffee":
        product = 0.50
    if product == "water":
        product = 0.80
    if product == "beer":
        product = 1.20
    if product == "sweets":
        product = 1.45
    if product == "peanuts":
        product = 1.60

elif town == "Plovdiv":
    if product == "coffee":
        product = 0.40
    if product == "water":
        product = 0.70
    if product == "beer":
        product = 1.15
    if product == "sweets":
        product = 1.30
    if product == "peanuts":
        product = 1.50

elif town == "Varna":
    if product == "coffee":
        product = 0.45
    if product == "water":
        product = 0.70
    if product == "beer":
        product = 1.10
    if product == "sweets":
        product = 1.35
    if product == "peanuts":
        product = 1.55

print(qty * product)