n = int(input())

for i in range(1111, 10000):
    i = str(i)
    count = 0
    for index, digit in enumerate(i):
        digit = int(digit)

        if digit == 0:
            continue

        if n % digit == 0:
            count += 1

        if count == 4:
            print(i, end=" ")
