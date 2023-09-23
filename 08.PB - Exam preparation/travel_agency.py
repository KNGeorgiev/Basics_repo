town = input()
package = input()
discount = input()
days = int(input())
price = 0

if days > 7:
    days -= 1

if town == "Borovets" or town == "Bansko":
    if package == "withEquipment":
        price = 100 * days
        if discount == "yes":
            price = price - price * 0.10
    if package == "noEquipment":
        price = 80 * days
        if discount == "yes":
            price = price - price * 0.05

if town == "Varna" or town == "Burgas":
    if package == "withBreakfast":
        price = 130 * days
        if discount == "yes":
            price = price - price * 0.12

    if package == "noBreakfast":
        price = 100 * days
        if discount == "yes":
            price = price - price * 0.07

if days < 1:
    print("Days must be positive number!")

elif town != "Borovets" and town != "Bansko" and town != "Varna" and town != "Burgas":
    print("Invalid input!")

elif package != "withEquipment" and package != "noEquipment" and package != "withBreakfast" and package != "noBreakfast":
    print("Invalid input!")

else:
    print(f"The price is {price:.2f}lv! Have a nice time!")