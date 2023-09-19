control_value = int(input())
count = 0
a2 = 0
b2 = 0
c2 = 0
d2 = 0

for a in range(1, 10):

    for b in range(1, 10):
        if a < b:

            for c in range(1, 10):

                for d in range(1, 10):
                    if c > d:
                        if (a * b) + (c * d) == control_value:
                            count += 1
                            print(f"{a}{b}{c}{d}", end=" ")
                            if count == 4:
                                a2 += a
                                b2 += b
                                c2 += c
                                d2 += d

if count >= 4:
    print(f"")
    print(f"Password: {a2}{b2}{c2}{d2}")

elif count < 4:
    print(f"")
    print(f"No!")