kilometres = int(input())
time = input()
price = 0

if kilometres < 20:
    if time == "day":
        price += 0.7 + 0.79 * kilometres
    elif time == "night":
        price += 0.7 + 0.90 * kilometres

elif 20 <= kilometres < 100:
    if time == "night" or time == "day":
        price += 0.09 * kilometres

elif 100 <= kilometres:
    if time == "night" or time == "day":
        price += 0.06 * kilometres

print(f"{price:.2f}")
