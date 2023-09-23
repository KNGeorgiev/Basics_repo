budget = float(input())
nights = int(input())
cost_per_night = float(input())
additional_percentage = int(input())

if nights > 7:
    cost_per_night = cost_per_night - cost_per_night * 0.05

total_cost = (nights * cost_per_night) + (budget * additional_percentage / 100)

if budget >= total_cost:
    print(f"Ivanovi will be left with {budget - total_cost:.2f} leva after vacation.")

if budget < total_cost:
    print(f"{total_cost - budget:.2f} leva needed.")
