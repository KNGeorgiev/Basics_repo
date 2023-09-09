# Да се напише конзолна програма, която прочита възраст (реално число) и пол ('m' или 'f'),
# въведени от потребителя, и отпечатва обръщение измежду следните:
# ⦁	"Mr." – мъж (пол 'm') на 16 или повече години
# ⦁	"Master" – момче (пол 'm') под 16 години
# ⦁	"Ms." – жена (пол 'f') на 16 или повече години
# ⦁	"Miss" – момиче (пол 'f') под 16 години

age = float(input())
gender = str(input())

if age >= 16 and gender == "m":
    print("Mr.")

elif age < 16 and gender == "m":
    print("Master")

elif age >= 16 and gender == "f":
    print("Ms.")

elif age < 16 and gender == "f":
    print("Miss")