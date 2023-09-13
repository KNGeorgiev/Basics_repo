start = int(input())
finish = int(input())
magic_number = int(input())
counter = 0
magic_counter = 0

for a in range(start, finish + 1):
    for b in range(start, finish + 1):
        counter += 1
        if a + b == magic_number:
            magic_counter += 1
            if magic_counter == 1:
                print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
                break

if magic_counter == 0:
    print(f"{counter} combinations - neither equals {magic_number}")