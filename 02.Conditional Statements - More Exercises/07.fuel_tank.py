fuel_type = input()
fuel_litres = float(input())

if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
    print("Invalid fuel!")

elif fuel_litres < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")

elif fuel_litres >= 25:
    print(f"You have enough {fuel_type.lower()}.")