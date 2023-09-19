day = int(input())
hours = int(input())
total = 0

for x in range(1, day + 1):
    day_total = 0

    for y in range(1, hours + 1):
        if y == 24:
            y = 0

        if x % 2 == 0:
            if y % 2 != 0:
                total += 2.5
                day_total += 2.5
            else:
                total += 1
                day_total += 1

        if x % 2 != 0:
            if y % 2 == 0:
                total += 1.25
                day_total += 1.25
            else:
                total += 1
                day_total += 1

    print(f"Day: {x} - {day_total:.2f} leva")

print(f"Total: {total:.2f} leva")
