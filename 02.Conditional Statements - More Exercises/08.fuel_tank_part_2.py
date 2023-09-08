gasoline = 2.22
diesel = 2.33
gas = 0.93

fuel_type = input()
fuel_quantity = float(input())
card_possession = input()

if fuel_type == "Gasoline":
    clean_price = gasoline * fuel_quantity
    if card_possession == "Yes":
        gasoline = gasoline - 0.18
        clean_price = gasoline * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        clean_price = clean_price - clean_price * 0.08
    if fuel_quantity > 25:
        clean_price = clean_price - clean_price * 0.1
elif fuel_type == "Diesel":
    clean_price = diesel * fuel_quantity
    if card_possession == "Yes":
        diesel = diesel - 0.12
        clean_price = diesel * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        clean_price = clean_price - clean_price * 0.08
    if fuel_quantity > 25:
        clean_price = clean_price - clean_price * 0.1
elif fuel_type == "Gas":
    clean_price = gas * fuel_quantity
    if card_possession == "Yes":
        gas = gas - 0.08
        clean_price = gas * fuel_quantity
    if 20 <= fuel_quantity <= 25:
        clean_price = clean_price - clean_price * 0.08
    if fuel_quantity > 25:
        clean_price = clean_price - clean_price * 0.1

print(f'{clean_price:.2f} lv.')
