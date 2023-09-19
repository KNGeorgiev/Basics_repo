prime = 0
non_prime = 0
command = input()

while command != "stop":
    command = int(command)

    if command < 0:
        print("Number is negative.")
        command = input()
        continue

    count = 0
    for x in range(1, command + 1):
        if (command % x) == 0:
            count += 1

    if count == 2:
        prime += command

    else:
        non_prime += command

    command = input()
print(f"Sum of all prime numbers is: {prime}\n"
      f"Sum of all non prime numbers is: {non_prime}")