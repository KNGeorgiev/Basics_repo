one_leva = int(input())
two_leva = int(input())
five_leva = int(input())
total_sum = int(input())

for x in range(0, one_leva + 1):

    for y in range(0, two_leva + 1):

        for z in range(0, five_leva + 1):
            if x * 1 + y * 2 + z * 5 == total_sum:
                print(f"{x} * 1 lv. + {y} * 2 lv. + {z} * 5 lv. = {total_sum} lv.")
