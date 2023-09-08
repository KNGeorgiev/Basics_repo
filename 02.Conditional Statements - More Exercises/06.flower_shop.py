import math

magnolii = 3.25
zumbuli = 4
rozi = 3.50
kaktusi = 8

magnolii_number = int(input())
zumbuli_number = int(input())
rozi_number = int(input())
kaktusi_number = int(input())
cena_na_podaruk = float(input())

total_profit = ((magnolii_number * magnolii) + (zumbuli_number * zumbuli) + \
               (rozi_number * rozi) + (kaktusi_number * kaktusi)) - \
               ((magnolii_number * magnolii) + (zumbuli_number * zumbuli) + \
               (rozi_number * rozi) + (kaktusi_number * kaktusi)) * 0.05

if cena_na_podaruk <= total_profit:
    print(f"She is left with {math.floor(total_profit - cena_na_podaruk)} leva.")

elif cena_na_podaruk > total_profit:
    print(f"She will have to borrow {math.ceil(cena_na_podaruk - total_profit)} leva.")
