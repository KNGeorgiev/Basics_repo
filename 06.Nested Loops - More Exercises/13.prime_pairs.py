first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input()) + first_pair_start
second_pair_diff = int(input()) + second_pair_start

for a in range(first_pair_start, first_pair_diff + 1):
    count1 = 0
    for x in range(2, a):
        if a % x == 0:
            count1 += 1
    if count1 == 0:

        for b in range(second_pair_start, second_pair_diff + 1):
            count2 = 0
            for y in range(2, b):
                if b % y == 0:
                    count2 += 1
            if count2 == 0:
                print(f"{a}{b}")
