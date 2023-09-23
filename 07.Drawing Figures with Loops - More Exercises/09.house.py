import math

a = int(input())
wall = math.ceil(a / 2)

if a % 2 != 0:
    for x in range(1, a + 1):
        dash = math.ceil((a - x) / 2)
        if x % 2 != 0:
            print("-" * dash + "*" * x + "-" * dash)
    for y in range(1, wall):
        print("|" + "*" * (a - 2) + "|")

if a % 2 == 0:
    for x in range(1, a + 1):
        dash = math.ceil((a - x) / 2)
        if x % 2 == 0:
            print("-" * dash + "*" * x + "-" * dash)

    for y in range(1, wall + 1):
        print("|" + "*" * (a - 2) + "|")
