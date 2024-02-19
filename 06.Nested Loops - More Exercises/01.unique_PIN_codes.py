first_number_range = int(input())
second_number_range = int(input())
third_number_range = int(input())

for first_num in range(1, first_number_range + 1):
    if first_num % 2 == 0:

        for second_num in range(2, second_number_range + 1):

            for third_num in range(1, third_number_range + 1):
                if third_num % 2 == 0:

                    if second_num == 2 or second_num == 3 or second_num == 5 or second_num == 7:
                        print(f"{first_num} {second_num} {third_num}")
