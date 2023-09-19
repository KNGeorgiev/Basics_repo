first_letter = input()
last_letter = input()
skip_letter = input()
count = 0

first_letter = ord(first_letter)
last_letter = ord(last_letter)
skip_letter = ord(skip_letter)

for l1 in range(first_letter, last_letter + 1):

    for l2 in range(first_letter, last_letter + 1):

        for l3 in range(first_letter, last_letter + 1):
            if l1 != skip_letter and l2 != skip_letter and l3 != skip_letter:
                count += 1
                print(f"{chr(l1)}{chr(l2)}{chr(l3)}", end=" ")
print(f"{count}", end=" ")