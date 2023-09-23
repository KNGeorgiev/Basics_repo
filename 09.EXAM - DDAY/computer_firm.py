computer_number = int(input())
rating_count = 0
sales_count = 0

for x in range(1, computer_number + 1):
    number = int(input())
    rating = number % 10
    rating_count += rating
    sales = number // 10

    if rating == 2:
        percentage = 0
        total = sales - sales
        sales_count += total

    if rating == 3:
        percentage = 0.50
        total = sales * percentage
        sales_count += total

    if rating == 4:
        percentage = 0.70
        total = sales * percentage
        sales_count += total

    if rating == 5:
        percentage = 0.85
        total = sales * percentage
        sales_count += total

    if rating == 6:
        percentage = 1
        total = sales
        sales_count += total

print(f"{sales_count:.2f}")
print(f"{rating_count / computer_number:.2f}")