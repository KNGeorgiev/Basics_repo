# Да се напише програма, която чете n-на брой цели числа,
# въведени от потребителя,и проверява дали сред тях съществува число,
# което е равно на сумата на всички останали.

# ⦁	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност

# ⦁	Ако няма такъв елемент печата "No"
# и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)


import sys

n = int(input())
max = -sys.maxsize
sum = 0

for i in range(n):
    num = int(input())
    sum += num
    if num > max:
        max = num

if max == sum - max:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {abs((sum - max) - max)}")
