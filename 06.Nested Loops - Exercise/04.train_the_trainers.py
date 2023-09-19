people = int(input())
presentation = input()
note_number = 0
total_notes = 0
total_average = 0

while presentation != "Finish":
    average = 0
    total_notes = 0

    for i in range(people):
        note = float(input())
        note_number += 1
        total_notes += note

        average = (total_notes / people)
        total_average += note
    print(f"{presentation} - {average:.2f}.")

    presentation = input()

print(f"Student's final assessment is {total_average / note_number:.2f}.")