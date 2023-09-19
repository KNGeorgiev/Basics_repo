last_sector = input()
first_sector_rows = int(input())
odd_places = int(input())
even_places = odd_places + 2
count = 0

for x in range(65, ord(last_sector) + 1):
    first_sector_rows += 1
    for row in range(1, first_sector_rows):
        if row % 2 != 0:
            for seat in range(97, 97 + odd_places):
                count += 1
                print(f"{chr(x)}{row}{chr(seat)}")

        if row % 2 == 0:
            for seat in range(97, 97 + even_places):
                count += 1
                print(f"{chr(x)}{row}{chr(seat)}")

print(count)