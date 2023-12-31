# Отговаряте за логистиката на различни товари.
# В зависимост от теглото на товара е нужно различно превозно средство.
# Цената на тон, за която се превозва товара е различна за всяко превозно средство:
# До 3 тона – микробус (200 лева на тон)
# От 4 до 11 тона – камион (175 лева на тон)
# 12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар,
# както и процента на тоновете  превозвани с всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).


load_number = int(input())
bus = 0
truck = 0
train = 0

for i in range(load_number):
    load_weight = int(input())
    if load_weight in range(4):
        bus += load_weight

    if load_weight in range(4, 12):
        truck += load_weight

    if load_weight >= 12:
        train += load_weight

total_weight = bus + truck + train
total_price = bus * 200 + truck * 175 + train * 120

print(f"{total_price / total_weight:.2f}")
print(f"{bus / total_weight * 100:.2f}%")
print(f"{truck / total_weight * 100:.2f}%")
print(f"{train / total_weight * 100:.2f}%")





