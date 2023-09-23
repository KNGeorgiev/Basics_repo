import math

a = int(input())

print(("*" * (2 * a)) + (" " * a) + ("*" * (2 * a)))

for x in range(1, a - 1):
    if x != math.ceil((a / 2) - 1) and a != 3:
        print("*" + "/" * (2 * a - 2) + "*" + (" " * a) + "*" + "/" * (2 * a - 2) + "*")

    if x == math.ceil((a / 2) - 1) or a == 3:
        print("*" + "/" * (2 * a - 2) + "*" + ("|" * a) + "*" + "/" * (2 * a - 2) + "*")

print(("*" * (2 * a)) + (" " * a) + ("*" * (2 * a)))