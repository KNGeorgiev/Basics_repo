collected_money = 0


while True:

    destination = input()

    if destination == "End":
        break

    min_budget = float(input())

    while collected_money < min_budget:
        new_destination = destination
        new_budget = min_budget
        saving = float(input())
        collected_money += saving

    if collected_money >= min_budget:
        print(f"Going to {destination}!")
        collected_money = 0