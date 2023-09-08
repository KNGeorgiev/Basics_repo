# Ресторант отваря врати и предлага няколко менюта на преференциални цени:
# ⦁	Пилешко меню –  10.35 лв.
# ⦁	Меню с риба – 12.40 лв.
# ⦁	Вегетарианско меню  – 8.15 лв.
# Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
# Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
# Цената на доставка е 2.50 лв и се начислява най-накрая.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Брой пилешки менюта – цяло число в интервала [0 … 99]
# ⦁	Брой менюта с риба – цяло число в интервала [0 … 99]
# ⦁	Брой вегетариански менюта – цяло число в интервала [0 … 99]
# Изход
# Да се отпечата на конзолата един ред:  "{цена на поръчката}"

chicken_menu = 10.35
fish_menu = 12.40
vegie_menu = 8.15
delivery = 2.50

num_chicken = int(input())
num_fish = int(input())
num_vegie = int(input())

total_chicken = num_chicken * chicken_menu
total_fish = num_fish * fish_menu
total_vegie = num_vegie * vegie_menu
total_menu_value = total_chicken + total_vegie + total_fish

desert = total_menu_value * 0.20
total_price = total_menu_value + desert + delivery

print(total_price)