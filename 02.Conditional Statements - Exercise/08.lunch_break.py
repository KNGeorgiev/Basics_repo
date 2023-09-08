# По време на обедната почивка искате да изгледате епизод от своя любим сериал.
# Вашата задача е да напишете програма, с която ще разберете дали имате достатъчно време да изгледате епизода.
# По време на почивката отделяте време за обяд и време за отдих. Времето за обяд ще бъде 1/8 от времето за почивка,
# а времето за отдих ще бъде 1/4 от времето за почивка.
# Вход
# От конзолата се четат 3 реда:
# ⦁	Име на сериал – текст
# ⦁	Продължителност на епизод  – цяло число в диапазона [10… 90]
# ⦁	Продължителност на почивката  – цяло число в диапазона [10… 120]
# Изход
# На конзолата да се изпише един ред:
# ⦁	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# ⦁	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
# Времето да се закръгли до най-близкото цяло число нагоре.


import math

series_name = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

lunch_n_rest = lunch_time + rest_time
series_time = break_duration - lunch_n_rest

if series_time >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(series_time - episode_duration)} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(episode_duration - series_time)} more minutes.")
