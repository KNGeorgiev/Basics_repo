# Петя има магазин за детски играчки.
# Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# ⦁	Пъзел - 2.60 лв.
# ⦁	Говореща кукла - 3 лв.
# ⦁	Плюшено мече - 4.10 лв.
# ⦁	Миньон - 8.20 лв.
# ⦁	Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# ⦁	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# ⦁	Брой пъзели - цяло число в интервала [0… 1000]
# ⦁	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# ⦁	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# ⦁	Брой миньони - цяло число в интервала [0 … 1000]
# ⦁	Брой камиончета - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# ⦁	Ако парите са достатъчни се отпечатва:
# ⦁	"Yes! {оставащите пари} lv left."
# ⦁	Ако парите НЕ са достатъчни се отпечатва:
# ⦁	"Not enough money! {недостигащите пари} lv needed."
#
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

puzzle_price = 2.60
doll_price = 3.00
teddy_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input())
puzzle_number = int(input())
doll_number = int(input())
teddy_number = int(input())
minion_number = int(input())
truck_number = int(input())

total_profit = puzzle_number * puzzle_price + \
               doll_number * doll_price + \
               teddy_number * teddy_price + \
               minion_number * minion_price + \
               truck_number * truck_price

total_num_sold = puzzle_number + doll_number + teddy_number + minion_number + truck_number

if total_num_sold >= 50:
    total_profit = total_profit - total_profit * 0.25

final_profit = total_profit - total_profit * 0.10

if final_profit >= trip_price:
    print(f"Yes! {final_profit - trip_price:.2f} lv left.")

elif final_profit < trip_price:
    print(f"Not enough money! {trip_price - final_profit:.2f} lv needed.")