# Дадено число е валидно, ако е в диапазона [100…200] или е 0.
# Да се напише програма, която чете цяло число, въведено от потребителя,
# и печата "invalid" ако въведеното число не е валидно.

num = float(input())

if num not in range(100, 201) and num != 0:
    print("invalid")

else:
    print()