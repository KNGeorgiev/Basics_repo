# Напишете програма, която чете цяло число, въведено от потребителя, и
# отпечатва ден от седмицата (на английски език), в граници [1...7] или
# отпечатва "Error" в случай, че въведеното число е невалидно.

day_num = int(input())

if day_num == 1:
    day = "Monday"

elif day_num == 2:
    day = "Tuesday"

elif day_num == 3:
    day = "Wednesday"

elif day_num == 4:
    day = "Thursday"

elif day_num == 5:
    day = "Friday"

elif day_num == 6:
    day = "Saturday"

elif day_num == 7:
    day = "Sunday"

else:
    day = "Error"

print(day)
