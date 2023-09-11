# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто. Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети може да стане това.

first_coin = 2*1
second_coin = 1
third_coin = 1/2
forth_coin = 1/5
fifth_coin = 1/10
sixth_coin = 1/20
seventh_coin = 1/50
eight_coin = 1/100
coin_number = 0
change = float(input())

while True:

    if change >= first_coin:
        coin_number += change // first_coin
        change = f"{change % first_coin:.2f}"
        change = float(change)

    if first_coin > change >= second_coin:
        coin_number += change // second_coin
        change = f"{change % second_coin:.2f}"
        change = float(change)

    if second_coin > change >= third_coin:
        coin_number += change // third_coin
        change = f"{change % third_coin:.2f}"
        change = float(change)

    if third_coin > change >= forth_coin:
        coin_number += change // forth_coin
        change = f"{change % forth_coin:.2f}"
        change = float(change)

    if forth_coin > change >= fifth_coin:
        coin_number += change // fifth_coin
        change = f"{change % fifth_coin:.2f}"
        change = float(change)

    if fifth_coin > change >= sixth_coin:
        coin_number += change // sixth_coin
        change = f"{change % sixth_coin:.2f}"
        change = float(change)

    if sixth_coin > change >= seventh_coin:
        coin_number += change // seventh_coin
        change = f"{change % seventh_coin:.2f}"
        change = float(change)

    if change >= eight_coin:
        change = float(change)
        coin_number += 1

    print(int(coin_number))
    break
