# Напишете програма, която прочита от конзолата име, фамилия, възраст и град и печата следното съобщение: "You are <firstName> <lastName>, a <age>-years old person from <town>."

name = input()
last_name = input()
age = int(input())
origin = input()

print(f"You are {name} {last_name}, a {age}-years old person from {origin}.")