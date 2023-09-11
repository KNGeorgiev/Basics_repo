# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден. Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си. Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня и когато постигне целта си да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

goal = 10000
total_steps = 0

while total_steps < goal:
    command = input()

    if command == "Going home":
        command = int(input())
        total_steps += command
        break

    else:
        command = int(command)
        total_steps += command

if total_steps > goal:
    print("Goal reached! Good job!")
    print(f"{(total_steps - goal)} steps over the goal!")
elif total_steps < goal:
    print(f"{goal - total_steps} more steps to reach goal.")