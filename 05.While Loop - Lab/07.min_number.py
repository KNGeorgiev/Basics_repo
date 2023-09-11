# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

import sys

num = input()
min = sys.maxsize

while num != "Stop":
    num = int(num)
    if num < min:
        min = num
    num = input()
print(min)