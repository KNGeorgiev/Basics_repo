# Напишете програма, която да пресмята резултата от игра. Първо получавате число, което показва колко хода ще продължи играта. После за всеки ход на играта ще получавате по едно ново число. Според интервала в който попада числото се прибавят точки. Ако числото е отрицателно или по-голямо 50, тогава то е невалидно. В началото на играта резултата е 0 и на всеки ход се прибавят точки по следният начин:
#
# От 0 до 9  20 % от числото
# От 10 до 19  30 % от числото
# От 20 до 29  40 % от числото
# От 30 до 39  50 точки
# От 40 до 50  100 точки
# Невалидно число  резултата се дели на 2
#
# Освен резултата програмата трябва да изкарва статистика за проценти числа в дадените интервали.
# Вход
# Входът се чете от конзолата:
# Първи ред - колко хода ще има по време на играта – цяло число в интервала [1...100]
# За всеки ход – числата, които се проверяват в кой интервал са – цели числа в интервала [-100...100]
# Изход
# Да се отпечата на конзолата 7 реда:
# 1ви ред: "{Краен резултат}"
# 2ри ред: "From 0 to 9: {процент в интервала}%"
# 3ти ред: "From 10 to 19: {процент в интервала}%"
# 4ти ред: "From 20 to 29: {процент в интервала}%"
# 5ти ред: "From 30 to 39: {процент в интервала}%"
# 6ти ред: "From 40 to 50: {процент в интервала}%"
# 7ми ред: "Invalid numbers: {процент в интервала}%"
# Всички числа трябва да са форматирана до вторият знак след запетаята.


turns_number = int(input())
first_range = 0
second_range = 0
third_range = 0
forth_range = 0
fifth_range = 0
total_points = 0
invalid = 0
for i in range(1, turns_number+1):
    number = int(input())
    if number in range(0, 10):
        total_points += number * 0.20
        first_range += 1
    if number in range(10, 20):
        total_points += number * 0.30
        second_range += 1
    if number in range(20, 30):
        total_points += number * 0.40
        third_range += 1
    if number in range(30, 40):
        total_points += 50
        forth_range += 1
    if number in range(40, 51):
        total_points += 100
        fifth_range += 1
    if number > 50 or number < 0:
        invalid += 1
        total_points /= 2

total_number = first_range + second_range + third_range + forth_range + fifth_range + invalid
print(f"{total_points:.2f}")
print(f"From 0 to 9: {first_range / total_number * 100:.2f}%")
print(f"From 10 to 19: {second_range / total_number * 100:.2f}%")
print(f"From 20 to 29: {third_range / total_number * 100:.2f}%")
print(f"From 30 to 39: {forth_range / total_number * 100:.2f}%")
print(f"From 40 to 50: {fifth_range / total_number* 100:.2f}%")
print(f"Invalid numbers: {invalid / total_number * 100:.2f}%")
