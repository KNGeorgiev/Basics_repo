# Дадено е цяло число – начален брой точки. Върху него се начисляват бонус точки по правилата,
# описани по-долу. Да се напише програма, която пресмята бонус точките,
# които получава числото и общия брой точки (числото + бонуса).
# ⦁	Ако числото е до 100 включително, бонус точките са 5;
# ⦁	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# ⦁	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# ⦁	Допълнителни бонус точки (начисляват се отделно от предходните):
# ⦁	За четно число  + 1 т.
# ⦁	За число, което завършва на 5  + 2 т.

num = int(input())

if num <= 100:
    bonus = 5

elif 100 < num <= 1000:
    bonus = num * 20 / 100

elif num > 1000:
    bonus = num * 10 / 100

if num % 2 == 0:
    add_bonus = 1

elif num % 10 == 5:
    add_bonus = 2

else:
    add_bonus = 0

print(bonus + add_bonus)
print(num + add_bonus + bonus)