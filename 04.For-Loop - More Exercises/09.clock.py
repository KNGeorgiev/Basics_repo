# Напишете програма, която отпечатва часовете в денонощието от 0:0 до 23:59,
# всеки на отделен ред.
# Часовете трябва да се изписват във формат "{час} : {минути}".
minutes = 0
hours = 0
for x in range(0, 24):
    hours = x
    if hours > 23:
        hours = 0

    for i in range(0, 60):
        minutes = i
        if minutes > 59:
            minutes = 0
            hours += 1
        print(f"{hours} : {minutes}")