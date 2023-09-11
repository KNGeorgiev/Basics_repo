# Напишете програма, която да отпечатва часовете в денонощието от 0:0:0 до 23:59:59, всеки на отделен ред.
# Часовете да се изписват във формат "{час} : {минути} : {секунди} ".
minutes = 0
hours = 0
seconds = 0
for x in range(0, 24):
    hours = x
    if hours > 23:
        hours = 0

    for i in range(60):
        minutes = i
        if minutes > 59:
            minutes = 0
            hours += 1

        for y in range(60):
            seconds = y
            if seconds > 59:
                seconds = 0
                minutes += 1
            print(f"{hours} : {minutes} : {seconds}")