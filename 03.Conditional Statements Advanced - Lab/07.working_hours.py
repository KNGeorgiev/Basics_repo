# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

time = int(input())
day = input()

if day == "Monday" and time in range(10, 19):
    print("open")

elif day == "Tuesday" and time in range(10, 19):
    print("open")

elif day == "Wednesday" and time in range(10, 19):
    print("open")

elif day == "Thursday" and time in range(10, 19):
    print("open")

elif day == "Friday" and time in range(10, 19):
    print("open")

elif day == "Saturday" and time in range(10, 19):
    print("open")

else:
    print("closed")