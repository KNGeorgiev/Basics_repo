male = int(input())
female = int(input())
max_table = int(input())
busy_table = 0

for x in range(1, male + 1):
    if busy_table == max_table:
        break
    for y in range(1, female + 1):
        busy_table += 1
        print(f"({x} <-> {y})", end=" ")
        if busy_table == max_table:
            break