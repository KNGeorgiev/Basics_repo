# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди, за което плува разстояние от 1 м.
# Да се напише програма, която изчислява дали се е справил със задачата, като се има предвид, че:
# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иванчо ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иванчо ще преплува разстоянието и разликата спрямо Световния рекорд.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Рекордът в секунди – реално число;
# ⦁	Разстоянието в метри – реално число;
# ⦁	Времето в секунди, за което плува разстояние от 1 м. - реално число.
# Изход
# Отпечатването на конзолата зависи от резултата:
# ⦁	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# ⦁	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# ⦁	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# ⦁	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

record = float(input())
distance_m = float(input())
time_1_m = (float(input()))

total_result = distance_m * time_1_m
resistance_time = (distance_m // 15) * 12.5
final_time = total_result + resistance_time

if record > final_time:
    print(f" Yes, he succeeded! The new world record is {final_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {final_time - record:.2f} seconds slower.")