days_off = int(input())
work_days = 365 - days_off
days_off_playtime = days_off * 127
work_days_playtime = work_days * 63
playtime_norm = 30000

total_playtime = days_off_playtime + work_days_playtime

if total_playtime > playtime_norm:
    print("Tom will run away")
    print(f"{(total_playtime - playtime_norm) // 60} hours and {(total_playtime - playtime_norm) % 60} minutes more for play")

elif total_playtime <= playtime_norm:
    print("Tom sleeps well")
    print(f"{(playtime_norm - total_playtime) // 60} hours and {(playtime_norm - total_playtime) % 60} minutes less for play")