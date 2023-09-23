daily_pocket_money = float(input())
daily_profit = float(input())
expenses = float(input())
gift_price = float(input())

final_money = (daily_pocket_money + daily_profit) * 5 - expenses

if final_money >= gift_price:
    print(f"Profit: {final_money:.2f} BGN, the gift has been purchased.")

elif final_money < gift_price:
    print(f"Insufficient money: {gift_price - final_money:.2f} BGN.")
    