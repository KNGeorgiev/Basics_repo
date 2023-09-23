a = int(input())

for x in range(1, a + 1):
    if x < a:
        print(" " * (a - x) + "* " * x)
    if x == a:
        for x in range(a, 0, -1):
            print(" " * (a - x) + "* " * x)
