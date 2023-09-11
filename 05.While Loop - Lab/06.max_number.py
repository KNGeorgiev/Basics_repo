# Напишете програма, която до получаване на командата "Stop",
# чете цели числа, въведени от потребителя,
# намира най-голямото измежду тях и го принтира.
# Въвежда се по едно число на ред.
import sys

num = input()
max = -sys.maxsize

while num != "Stop":
    num = int(num)
    if num > max:
        max = num
    num = input()
print(max)