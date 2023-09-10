# Дадени са n цели числа в интервала [1…1000].
# От тях някакъв процент p1 са под 200,
# друг процент p2 са от 200 до 399, друг процент p3 са от 400 до 599,
# друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре.
# Да се напише програма, която изчислява и
# отпечатва процентите p1, p2, p3, p4 и p5.

n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, n + 1):
    num = int(input())
    if 1 <= num <= 199:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif 800 <= num <= 1000:
        p5 += 1

print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")