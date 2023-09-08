# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
# Важат следните цени:
# ⦁	Видеокарта – 250 лв./бр.
# ⦁	Процесор – 35% от цената на закупените видеокарти/бр.
# ⦁	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# ⦁	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# ⦁	Броят видеокарти - цяло число в интервала [1…100]
# ⦁	Броят процесори - цяло число в интервала [1…100]
# ⦁	Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# ⦁	Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# ⦁	Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.

budget = float(input())
gpu_number = int(input())
cpu_number = int(input())
ram_number = int(input())

gpu_price = 250
cpu_price = gpu_price * gpu_number * 0.35
ram_price = gpu_price * gpu_number * 0.10

total_price = (gpu_price * gpu_number) + (cpu_price * cpu_number) + (ram_price * ram_number)

if gpu_number > cpu_number:
    total_price = total_price - total_price * 0.15

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")

else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
