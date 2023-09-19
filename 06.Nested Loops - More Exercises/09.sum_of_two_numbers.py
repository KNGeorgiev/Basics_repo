interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
count = 0
magic_counter = 0

for x in range(interval_start, interval_end +1):
    for y in range(interval_start, interval_end +1):
        count += 1
        if x + y == magic_number:
            magic_counter += 1
            if magic_counter == 1:
                print(f"Combination N:{count} ({x} + {y} = {magic_number})")
                break

if magic_counter == 0:
    print(f"{count} combinations - neither equals {magic_number}")