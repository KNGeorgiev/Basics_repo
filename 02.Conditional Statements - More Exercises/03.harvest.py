import math

vineyard_area = int(input())
grapes_kg_per_sqm = float(input())
needed_wine = int(input())
workers = int(input())

total_harvest = vineyard_area * grapes_kg_per_sqm
wine_produced = 0.4 * total_harvest / 2.5

if wine_produced < needed_wine:
    print(f"It will be a tough winter! More {math.floor(needed_wine - wine_produced)} liters wine needed.")

elif wine_produced >= needed_wine:
    print(f"Good harvest this year! Total wine: {math.floor(wine_produced)} liters.")
    print(f"{math.ceil(wine_produced - needed_wine)} liters left -> {math.ceil((wine_produced - needed_wine) / workers)} liters per person.")
