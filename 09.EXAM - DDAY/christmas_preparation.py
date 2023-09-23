paper = 5.80
textile = 7.20
glue = 1.20

paper_number = int(input())
textile_number = int(input())
glue_number = float(input())
discount = float(input())

paper_price = paper_number * paper
textile_price = textile_number * textile
glue_price = glue_number * glue

total = paper_price + textile_price + glue_price
total_with_discount = total - total * (discount / 100)

print(f"{total_with_discount:.3f}")