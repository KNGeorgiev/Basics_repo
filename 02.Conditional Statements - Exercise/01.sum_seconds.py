# Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат "минути:секунди".
# Секундите да се изведат с водеща нула (2  "02", 7  "07", 35  "35").

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third
total_time_minutes = total_time // 60
total_time_seconds = total_time - total_time_minutes * 60

if total_time_seconds <10:
    print(f"{total_time_minutes}:0{total_time_seconds}")
else:
    print(f"{total_time_minutes}:{total_time_seconds}")
    
