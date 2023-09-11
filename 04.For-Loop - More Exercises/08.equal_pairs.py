count = int(input())
previous_sum = int(input()) + int(input())
max_dif = 0

for i in range(count - 1):
    current_sum = int(input()) + int(input())

    if abs(previous_sum - current_sum) > max_dif:
        max_dif = abs(previous_sum - current_sum)

    previous_sum = current_sum

if max_dif == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_dif}")