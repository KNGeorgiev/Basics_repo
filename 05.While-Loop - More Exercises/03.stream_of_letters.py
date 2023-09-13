import string

word1 = ""
word2 = ""
command = ""

letter = input()
while True:

    if letter == "End":
        break

    if letter not in string.ascii_letters:
        letter = input()
        continue

    if (letter == "c" and "c" not in word2) or \
            (letter == "n" and "n" not in word2) or \
            (letter == "o" and "o" not in word2):
        word2 += letter
    else:
        word1 += letter

    letter = input()

    if "c" in word2 and "n" in word2 and "o" in word2:
        word1 += ""
        print(word1, end=" ")
        word1 = ""
        word2 = ""