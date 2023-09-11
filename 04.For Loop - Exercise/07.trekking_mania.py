# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
# Според размера на групата, катерачите ще изкачват различни върхове.

# ⦁	Група до 5 човека – изкачват Мусала
# ⦁	Група от 6 до 12 човека – изкачват Монблан
# ⦁	Група от 13 до 25 човека – изкачват Килиманджаро
# ⦁	Група от 26 до 40 човека –  изкачват К2
# ⦁	Група от 41 или повече човека – изкачват Еверест

# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.

# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# ⦁	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# ⦁	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]

# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00% с точност до втората цифра след десетичната запетая.
# ⦁	Първи ред - процентът изкачващи Мусала
# ⦁	Втори ред – процентът изкачващи Монблан
# ⦁	Трети ред – процентът изкачващи Килиманджаро
# ⦁	Четвърти ред – процентът изкачващи К2
# ⦁	Пети ред – процентът изкачващи Еверест

group_number = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(group_number):
    ppl_num = int(input())
    if ppl_num in range(1, 6):
        musala += ppl_num
    elif ppl_num in range(6, 13):
        montblanc += ppl_num
    elif ppl_num in range(13, 26):
        kilimanjaro += ppl_num
    elif ppl_num in range(26, 41):
        k2 += ppl_num
    elif ppl_num >= 41:
        everest += ppl_num

total_ppl = (musala + montblanc + kilimanjaro + k2 + everest)
print(f"{musala / total_ppl * 100:.2f}%")
print(f"{montblanc / total_ppl * 100:.2f}%")
print(f"{kilimanjaro / total_ppl * 100:.2f}%")
print(f"{k2 / total_ppl * 100:.2f}%")
print(f"{everest / total_ppl * 100:.2f}%")