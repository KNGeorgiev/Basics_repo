# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# ⦁	За нечетните рождени дни (1, 3, 5...n) получава играчки.
# ⦁	За четните рождени дни (2, 4, 6...n) получава пари.
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв.,
# за всеки следващ четен рожден ден (2 -> 10, 4 -> 20, 6 -> 30...и т.н.).
# През годините Лили тайно е спестявала парите. Братът на Лили,
# в годините, които тя получава пари, взима по 1.00 лев от тях.
# Лили продала играчките получени през годините, всяка за P лева и добавила сумата към спестените пари.
# С парите искала да си купи пералня за X лева. Напишете програма, която да пресмята,
# колко пари е събрала и дали ѝ стигат да си купи пералня.
# Вход
# Програмата прочита 3 числа, въведени от потребителя, на отделни редове:
# ⦁	Възрастта на Лили - цяло число в интервала [1...77]
# ⦁	Цената на пералнята - число в интервала [1.00...10 000.00]
# ⦁	Единична цена на играчка - цяло число в интервала [0...40]
# Изход
# Да се отпечата на конзолата един ред:
# ⦁	Ако парите на Лили са достатъчни:
# ⦁	"Yes! {N}" - където N е остатъка пари след покупката
# ⦁	Ако парите не са достатъчни:
# ⦁	"No! {М}" - където M е сумата, която не достига
# Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.

n = int(input())
washing_machine = float(input())
toy_price = int(input())

money = 0
toy_number = 0
brother = 0
total_money = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        money = money + 10
        total_money += money
        brother += 1
    else:
        toy_number += 1

total_money = total_money + toy_number * toy_price - brother

if total_money >= washing_machine:
    print(f"Yes! {total_money - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - total_money:.2f}")






