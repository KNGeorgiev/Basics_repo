k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitutes = 0
flag = False

for num1 in range(k, 9):
    for num2 in range(9, l - 1, -1):
        for num3 in range(m, 9):
            for num4 in range(9, n - 1, -1):

                if num1 % 2 == 0 and num3 % 2 == 0 and num2 % 2 != 0 and num4 % 2 != 0:
                    first_player = f"{num1}{num2}"
                    second_player = f"{num3}{num4}"

                    if first_player == second_player:
                        print("Cannot change the same player.")
                    else:
                        substitutes += 1
                        print(f"{first_player} - {second_player}")
                        if substitutes >= 6:
                            flag = True

                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break