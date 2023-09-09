# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:
#
# Град	0 ≤ s ≤ 500 || 500 < s ≤ 1 000 || 1 000 < s ≤ 10 000 ||	s > 10 000
# Sofia	    5%	             7%	                  8%	          12%
# Varna	    4.5%	         7.5%	              10%	          13%
# Plovdiv	5.5%	         8%	                  12%	          14.5%
#
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число),
# въведени от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица.
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка.
# При невалиден град или обем на продажбите (отрицателно число) да се отпечата "error".

town = str(input())
sales = float(input())
commission = 0

town_list = ["Sofia", "Varna", "Plovdiv"]

if town in town_list and 0 <= sales <= 500:
    if town == "Sofia":
        commission = sales * 0.05
    elif town == "Varna":
        commission = sales * 0.045
    elif town == "Plovdiv":
        commission = sales * 0.055
    print(f"{commission:.2f}")

elif town in town_list and 500 < sales <= 1000:
    if town == "Sofia":
        commission = sales * 0.07
    elif town == "Varna":
        commission = sales * 0.075
    elif town == "Plovdiv":
        commission = sales * 0.08
    print(f"{commission:.2f}")

elif town in town_list and 1000 < sales <= 10000:
    if town == "Sofia":
        commission = sales * 0.08
    elif town == "Varna":
        commission = sales * 0.10
    elif town == "Plovdiv":
        commission = sales * 0.12
    print(f"{commission:.2f}")

elif town in town_list and sales > 10000:
    if town == "Sofia":
        commission = sales * 0.12
    elif town == "Varna":
        commission = sales * 0.13
    elif town == "Plovdiv":
        commission = sales * 0.145
    print(f"{commission:.2f}")

else:
    print("error")
