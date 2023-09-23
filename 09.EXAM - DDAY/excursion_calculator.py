people_number = int(input())
season = input()
price = 0

if season == "spring":
    if people_number <= 5:
        price = 50.00
    elif people_number > 5:
        price = 48.00

    total = people_number * price

elif season == "summer":
    if people_number <= 5:
        price = 48.50
    elif people_number > 5:
        price = 45.00

    total = (people_number * price) - (people_number * price) * 0.15

elif season == "autumn":
    if people_number <= 5:
        price = 60.00
    elif people_number > 5:
        price = 49.50

    total = people_number * price

elif season == "winter":
    if people_number <= 5:
        price = 86.00
    elif people_number > 5:
        price = 85.00

    total = (people_number * price) + (people_number * price) * 0.08

print(f"{total:.2f} leva.")
