# Да се напише програма, която чете текст (стринг),
# въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:
# буква	    a	e	i	o	u
# стойност	1	2	3	4	5

word = input()
number = 0

for i in word:
    if i == "a":
        number += 1
    if i == "e":
        number += 2
    if i == "i":
        number += 3
    if i == "o":
        number += 4
    if i == "u":
        number += 5

print(number)
