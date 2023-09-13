total_floor = int(input())
total_room = int(input())

for floor in range(total_floor, 0, -1):
    for room in range(0, total_room):

        if floor % 2 == 0:
            type = "O"

        else:
            type = "A"

        if floor == total_floor:
            type = "L"

        print(f"{type}{floor}{room}", end= " ")
    print( )


