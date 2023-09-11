# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# ⦁	Пари, нужни за екскурзията - реално число;
# ⦁	Налични пари - реално число.
# След това многократно се четат по два реда:
# ⦁	Вид действие – текст с две възможности: "spend" или "save";
# ⦁	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# ⦁	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# ⦁	"You can't save the money."
# ⦁	"{Общ брой изминали дни}"
# ⦁	Ако Джеси събере парите за почивката, на конзолата се изписва:
# ⦁	"You saved the money for {общ брой изминали дни} days."


needed_money = float(input())
available_money = float(input())
spend_days_number = 0
total_days = 0

while needed_money > available_money:
    action = input()
    money_amount = float(input())
    total_days += 1

    if action == "spend":
        spend_days_number += 1
        available_money -= money_amount
        if available_money - money_amount <= 0:
            available_money = 0

    if action == "save":
        available_money += money_amount
        spend_days_number = 0

    if spend_days_number >= 5:
        print("You can't save the money.")
        print(f"{total_days}")
        break

    if available_money >= needed_money:
        print(f"You saved the money for {total_days} days.")
        break