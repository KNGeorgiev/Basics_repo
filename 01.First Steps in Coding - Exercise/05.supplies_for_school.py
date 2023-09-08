# Учебната година вече е започнала и отговорничката на 10Б клас - Ани трябва да купи определен брой пакетчета с химикали, пакетчета с маркери, както и препарат за почистване на дъска. Тя е редовна клиентка на една книжарница, затова има намаление за нея, което представлява някакъв процент от общата сума. Напишете програма, която изчислява колко пари ще трябва да събере Ани, за да плати сметката, като имате предвид следния ценоразпис:
# ⦁	Пакет химикали - 5.80 лв.
# ⦁	Пакет маркери - 7.20 лв.
# ⦁	Препарат - 1.20 лв (за литър)
# Вход
# От конзолата се четат 4 числа:
# ⦁	Брой пакети химикали - цяло число в интервала [0...100]
# ⦁	Брой пакети маркери - цяло число в интервала [0...100]
# ⦁	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
# ⦁	Процент намаление - цяло число в интервала [0...100]
# Изход
# Да се отпечата на конзолата колко пари ще са нужни на Ани, за да си плати сметката.

pen_price = 5.80
marker_price = 7.20
cleaning_detergent_price = 1.20

pen_number = int(input())
marker_number = int(input())
detergent_litres = int(input())
discount_percentage = int(input())

total_pen_value = pen_number * pen_price
total_marker_value = marker_number * marker_price
total_detergent_value = detergent_litres * cleaning_detergent_price


total_money = total_pen_value + total_marker_value + total_detergent_value
total_discount = total_money - (total_money * discount_percentage) / 100
print(total_discount)