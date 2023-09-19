sum = int(input())

for i in range(1111, 10000):
    sum_to_string = str(i)

    first_pos = 0
    second_pos = 0
    third_pos = 0
    forth_pos = 0
    first_couple = 0
    second_couple = 0

    for index, digit in enumerate(sum_to_string):
        if index == 0:
            if int(digit) != 0:
                first_pos += int(digit)

        if index == 1:
            if int(digit) != 0:
                second_pos += int(digit)

        if index == 2:
            if int(digit) != 0:
                third_pos += int(digit)

        if index == 3:
            if int(digit) != 0:
                forth_pos += int(digit)

    first_couple = first_pos + second_pos
    second_couple = third_pos + forth_pos

    if first_pos != 0 and second_pos != 0 and third_pos != 0 and forth_pos != 0:
        if first_couple == second_couple:
            if sum % first_couple == 0 and sum % second_couple == 0:
                print(i, end=" ")
