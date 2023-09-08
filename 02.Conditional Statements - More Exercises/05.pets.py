import math

days = int(input())
left_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

turtle_kilos = turtle_food / 1000
total_food_per_day = dog_food + cat_food + turtle_kilos
total_food = days * total_food_per_day

if left_food >= total_food:
    print(f"{math.floor(left_food - total_food)} kilos of food left.")

elif left_food < total_food:
    print(f"{math.ceil(total_food - left_food)} more kilos of food are needed.")
    