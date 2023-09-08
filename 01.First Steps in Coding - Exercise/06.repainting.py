# Румен иска да пребоядиса хола и за целта е наел майстори. Напишете програма, която изчислява разходите за ремонта, предвид следните цени:
# ⦁	Предпазен найлон - 1.50 лв. за кв. метър
# ⦁	Боя - 14.50 лв. за литър
# ⦁	Разредител за боя - 5.00 лв. за литър
# За всеки случай, към необходимите материали, Румен иска да добави още 10% от количеството боя и 2 кв.м. найлон, разбира се и 0.40 лв. за торбички. Сумата, която се заплаща на майсторите за 1 час работа, е равна на 30% от сбора на всички разходи за материали.
# Вход
# Входът се чете от конзолата и съдържа точно 4 реда:
# ⦁	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
# ⦁	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
# ⦁	Количество разредител (в литри) - цяло число в интервала [1…30]
# ⦁	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# Изход
# Да се отпечата на конзолата един ред:
# ⦁	"{сумата на всички разходи}"

plastic_price = 1.50
paint_price = 14.50
corselin_price = 5.00

plastic_qty = int(input())
paint_qty = int(input())
corselin_qty = int(input())
working_hours = int(input())

total_plastic_price = plastic_price * (plastic_qty + 2)
total_paint_price = paint_price * (paint_qty + (paint_qty * 0.10))
total_corselin_price = corselin_price * corselin_qty
plastic_bags = 0.40

total_mat_price = (total_plastic_price + total_paint_price + total_corselin_price + 0.40)
working_price = working_hours * (total_mat_price * 0.30)

total_expenses = total_mat_price + working_price
print(total_expenses)