# За даден период от време, всеки ден в болницата пристигат пациенти за преглед.
# Тя разполага първоначално със 7 лекари. Всеки лекар може да преглежда само по един пациент на ден,
# но понякога има недостиг на лекари, затова останалите пациенти се изпращат в други болници.
# Всеки трети ден, болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям от броя на прегледаните,
# се назначава още един лекар. Като назначаването става преди да започне приемът на пациенти за деня.
# Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
# Вход
# Входът се чете от конзолата и съдържа:
# На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# На следващите редове(равни на броят на дните) – броя пациенти, които пристигат за преглед за текущия ден. Цяло число в интервала [0…10 000]
# Изход
# Да се отпечатат на конзолата 2 реда :
# На първия ред: "Treated patients: {брой прегледани пациенти}."
# На втория ред: "Untreated patients: {брой непрегледани пациенти}."


period = int(input())
treated = 0
untreated = 0
doctor_number = 7

for i in range(1, period + 1):
    patient_number = int(input())
    if i % 3 != 0:
        if patient_number > doctor_number:
            treated += doctor_number
            untreated += patient_number - doctor_number
        elif patient_number <= doctor_number:
            treated += patient_number

    if i % 3 == 0:
        if untreated > treated:
            doctor_number += 1
        if patient_number > doctor_number:
            treated += doctor_number
            untreated += patient_number - doctor_number
        elif patient_number <= doctor_number:
            treated += patient_number

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")



