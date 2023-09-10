# Да се напише програма, която чете n-на брой цели числа,
# подадени от потребителя и проверява дали сумата от
# числата на четни позиции е равна на сумата на числата на нечетни позиции.
# ⦁	Ако сумите са равни да се отпечатат два реда: "Yes" и на нов ред "Sum = " + сумата;
# ⦁	Ако сумите не са равни да се отпечат два реда: "No" и на нов ред "Diff = " + разликата.
# Разликата се изчислява по абсолютна стойност.

n = int(input())
even = 0
odd = 0

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        even += num
    else:
        odd += num

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {abs(odd - even)}")