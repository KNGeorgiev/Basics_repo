# Магазин за плодове през работните дни работи на следните цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	    2.70	5.50	    3.85

# През събота и неделя магазинът работи на по-високи цени:

# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	    3.00	5.60	    4.20

# Напишете програма, която чете от конзолата следните три променливи, въведени от потребителя,
# и пресмята цената според цените от таблиците по-горе:
# ⦁	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# ⦁	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# ⦁	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".

product = str(input())
day = str(input())
quantity = float(input())

fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if day in working_days and product in fruits:
    if product == "banana":
        product = 2.50

    elif product == "apple":
        product = 1.20

    elif product == "orange":
        product = 0.85

    elif product == "grapefruit":
        product = 1.45

    elif product == "kiwi":
        product = 2.70

    elif product == "pineapple":
        product = 5.50

    elif product == "grapes":
        product = 3.85
    print(f"{product * quantity:.2f}")

elif day in weekend and product in fruits:
    if product == "banana":
        product = 2.70

    elif product == "apple":
        product = 1.25

    elif product == "orange":
        product = 0.90

    elif product == "grapefruit":
        product = 1.60

    elif product == "kiwi":
        product = 3.00

    elif product == "pineapple":
        product = 5.60

    elif product == "grapes":
        product = 4.20
    print(f"{product * quantity:.2f}")

else:
    print("error")