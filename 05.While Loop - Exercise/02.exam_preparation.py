# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка. Програмата трябва да приключи прочитането на данни при команда "Enough"
# или ако Марин получи определения брой незадоволителни оценки.
# Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
# ⦁	На първи ред - брой незадоволителни оценки - цяло число;
# ⦁	След това многократно се четат по два реда:
# ⦁	Име на задача – текст;
# ⦁	Оценка - цяло число в интервала [2…6]
# Изход
# ⦁	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# ⦁	"Average score: {средна оценка}"
# ⦁	"Number of problems: {броя на всички задачи}"
# ⦁	"Last problem: {името на последната задача}"
# ⦁	Ако получи определеният брой незадоволителни оценки:
# ⦁	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.


bad_grades_limit = int(input())
problem_number = 0
last_problem = 0
total_score = 0
bad_score_number = 0

while True:
    problem_name = input()

    if problem_name == "Enough":
        print(f"Average score: {total_score / problem_number:.2f}")
        print(f"Number of problems: {problem_number}")
        print(f"Last problem: {last_problem}")
        break

    problem_score = int(input())

    if problem_score <= 4:
        bad_score_number += 1

    if bad_score_number >= bad_grades_limit:
        print(f"You need a break, {bad_score_number} poor grades.")
        break

    problem_number += 1
    total_score += problem_score
    last_problem = problem_name
















