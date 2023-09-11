# Напишете програма, която първоначално прочита име и парола на потребителски профил.
# След това чете парола за вход.
# ⦁	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# ⦁	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

username = input()
password1 = input()

while True:
    password2 = input()
    if password1 == password2:
        break
print(f"Welcome {username}!")