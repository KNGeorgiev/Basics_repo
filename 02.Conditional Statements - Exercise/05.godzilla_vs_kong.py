# Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
# дали предвидените средства са достатъчни за снимането на филма. За снимките
# ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# ⦁	Декорът за филма е на стойност 10% от бюджета.
# ⦁	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# ⦁	Брой на статистите – цяло число в интервала [1 … 500]
# ⦁	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# ⦁	Ако  парите за декора и дрехите са повече от бюджета:
# ⦁	"Not enough money!"
# ⦁	"Wingard needs {парите недостигащи за филма} leva more."
# ⦁	Ако парите за декора и дрехите са по малко или равни на бюджета:
# ⦁	"Action!"
# ⦁	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

film_budget = float(input())
number_of_extras = int(input())
costume_price = float(input())

film_setting = film_budget * 0.10

if number_of_extras > 150:
    costume_price = costume_price - costume_price * 0.10

film_cost = number_of_extras * costume_price + film_setting

if film_cost > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {film_cost - film_budget:.2f} leva more.")

else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - film_cost:.2f} leva left.")