a = int(input())
b = int(input())
c = int(input())

for x in range(1, a + 1):
    if x % 2 == 0:
        for y in range(1, b + 1):
            if y == 2 or y == 3 or y == 5 or y == 7:
                for z in range(1, c + 1):
                    if z % 2 == 0:
                        print(f"{x} {y} {z}")