wanted_profit = float(input())
real_profit = 0

while real_profit < wanted_profit:
    cocktail_name = input()

    if cocktail_name == "Party!":
        print(f"We need {wanted_profit - real_profit:.2f} leva more.")
        print(f"Club income - {real_profit:.2f} leva.")
        break
    else:
        cocktail_number = int(input())
        cocktail_price = len(cocktail_name)

        real_profit += cocktail_number * cocktail_price

        if (cocktail_price * cocktail_number) % 2 != 0:
            real_profit -= (cocktail_price * cocktail_number) * 0.25

if real_profit >= wanted_profit:
    print("Target acquired.")
    print(f"Club income - {real_profit:.2f} leva.")
    
