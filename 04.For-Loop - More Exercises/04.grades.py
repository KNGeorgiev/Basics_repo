# Напишете програма, която да пресмята статистика на оценки от изпит.
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече.
# Също така и средният успех на изпита.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# "Top students: {процент студенти с успех 5.00 или повече}%"
# "Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# "Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# "Fail: {по-малко от 3.00}%"
# "Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.


student_number = int(input())
top_students = 0
lower_tier_1 = 0
lower_tier_2 = 0
fail = 0
total_grade_value = 0

for i in range(1, student_number + 1):
    student_grade = float(input())
    if student_grade >= 5:
        top_students += 1
        total_grade_value += student_grade
    if 4 <= student_grade < 5:
        lower_tier_1 += 1
        total_grade_value += student_grade
    if 3 <= student_grade < 4:
        lower_tier_2 += 1
        total_grade_value += student_grade
    if student_grade < 3:
        fail += 1
        total_grade_value += student_grade

print(f"Top students: {top_students / student_number * 100:.2f}%")
print(f"Between 4.00 and 4.99: {lower_tier_1 / student_number * 100:.2f}%")
print(f"Between 3.00 and 3.99: {lower_tier_2 / student_number * 100:.2f}%")
print(f"Fail: {fail / student_number * 100:.2f}%")
print(f"Average: {total_grade_value / student_number:.2f}")




