# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат за съдомиялна е достатъчно, за да измие определено количество съдове. Знае се, че всяка бутилка съдържа 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.  Приемете, че на всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери, а останалите пъти с чинии. Докато не получите команда "End" ще продължите да получавате бройка съдове, които трябва да бъдат измити.
# Вход
# От конзолата се четат:
# Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи, брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
# Изход
# В случай, че количеството препарат е било достатъчно за измиването на съдовете:
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"

dtg_bottle_num = int(input())
dtg_bottle_vol = 750
total_dtg = dtg_bottle_num * dtg_bottle_vol
plate_vol = 5
pot_vol = 15
plate_num = 0
pot_num = 0
place_in_washer = 0

while total_dtg >= 0:
    command = input()

    if command == "End":
        break

    if command != "End":
        command = int(command)
        place_in_washer += 1

        if place_in_washer % 3 == 0:
            current_pot = command * pot_vol
            pot_num += command
            total_dtg -= current_pot

        elif place_in_washer % 3 != 0:
            current_plate = command * plate_vol
            plate_num += command
            total_dtg -= current_plate

if total_dtg >= 0:
    print(f"Detergent was enough!\n"
          f"{plate_num} dishes and {pot_num} pots were washed.\n"
          f"Leftover detergent {total_dtg} ml.")

else:
    print(f"Not enough detergent, {abs(total_dtg)} ml. more necessary!")
