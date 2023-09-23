import math

a = int(input())
wall = math.ceil(a / 2)

if a % 2 != 0:
    for x in range(1, a + 1):
        dash = math.ceil((a - x) / 2)
        if x % 2 != 0:
            if x == 1:
                print("-" * dash + "*" + "-" * (x - 2) + "-" * dash)
            else:
                print("-" * dash + "*" + "-" * (x - 2) + "*" + "-" * dash)
        if x == a:
            for y in range(a - 1, 0, -1):
                dash = math.ceil((a - y) / 2)
                if y % 2 != 0:
                    if y == 1:
                        print("-" * dash + "*" + "-" * (y - 2) + "-" * dash)
                    else:
                        print("-" * dash + "*" + "-" * (y - 2) + "*" + "-" * dash)

if a % 2 == 0:
    for x in range(1, a + 1):
        dash = math.ceil((a - x) / 2)
        if x % 2 == 0:
            if x == 1:
                print("-" * dash + "*" + "-" * (x - 2) + "-" * dash)
            else:
                print("-" * dash + "*" + "-" * (x - 2) + "*" + "-" * dash)
        if x == a:
            for y in range(a - 1, 1, -1):
                dash = math.ceil((a - y) / 2)
                if y % 2 != 0:
                    if y == 1:
                        print("-" * dash + "*" + "-" * (y - 3) + "-" * dash)
                    else:
                        print("-" * dash + "*" + "-" * (y - 3) + "*" + "-" * dash)