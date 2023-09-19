lower = int(input())
upper = int(input())

for i in range(1111, 10000):
    num_to_str = str(i)

    first_pos = 0
    second_pos = 0
    third_pos = 0
    forth_pos = 0

    for index, digit in enumerate(num_to_str):

        if index == 0 and int(digit) != 0:
            first_pos = int(digit)

        if index == 1 and int(digit) != 0:
            second_pos = int(digit)

        if index == 2 and int(digit) != 0:
            third_pos = int(digit)

        if index == 3 and int(digit) != 0:
            forth_pos = int(digit)

    if first_pos in range(lower, upper + 1) and second_pos in range(lower, upper + 1)\
    and third_pos in range(lower, upper +1) and forth_pos in range(lower, upper + 1):
        if first_pos % 2 == 0 and forth_pos % 2 != 0:
            if first_pos > forth_pos:
                if (second_pos + third_pos) % 2 == 0:
                    print(i, end=" ")

        elif first_pos % 2 != 0 and forth_pos % 2 == 0:
            if first_pos > forth_pos:
                if (second_pos + third_pos) % 2 == 0:
                    print(i, end=" ")