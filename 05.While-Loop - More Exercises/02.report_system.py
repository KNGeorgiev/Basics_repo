# На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане с карта. Установени са следните правила за заплащане:
# Ако продуктът надвишава 100лв., за него не може да се плати в брой
# Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
# Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
# Вход
# От конзолата се четат:
# Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
# На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства: цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
# Изход
# На конзолата да се отпечата:
# При успешна транзакция: "Product sold!"
# При неуспешна транзакция: "Error in transaction!"
# Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да приключи и на конзолата да се изпишат два реда:
# "Average CS: {средно плащане в кеш на човек}"
# "Average CC: {средно плащане с карта на човек}"
#               Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
# При получаване на команда "End", да се изпише един ред:
# "Failed to collect required money for charity."


needed_sum = int(input())
donated_sum = 0
cash = 0
cash_sum = 0
card = 0
card_sum = 0
transaction_number = 0

while donated_sum < needed_sum:
    transaction = input()

    if transaction == "End":
        print("Failed to collect required money for charity.")
        break

    elif transaction != "End":
        transaction = int(transaction)
        transaction_number += 1

        if transaction_number % 2 != 0:
            if transaction > 100:
                print("Error in transaction!")

            else:
                cash += 1
                cash_sum += transaction
                donated_sum += transaction
                print("Product sold!")

        else:
            if transaction <= 10:
                print("Error in transaction!")

            else:
                card += 1
                card_sum += transaction
                donated_sum += transaction
                print("Product sold!")

if donated_sum >= needed_sum:
    print(f"Average CS: {cash_sum / cash:.2f}")
    print(f"Average CC: {card_sum / card:.2f}")