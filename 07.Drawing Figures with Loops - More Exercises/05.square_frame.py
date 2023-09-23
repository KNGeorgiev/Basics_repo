a = int(input())

print(f"+", "- " * (a - 2) + "+")
for x in range(2, a):
    print("|","- " * (a - 2) + "|")

print(f"+", "- " * (a - 2) + "+")