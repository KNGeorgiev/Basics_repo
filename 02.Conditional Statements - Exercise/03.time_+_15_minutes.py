# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути.
# Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.


hours = int(input())
minutes = int(input())

total_minutes = minutes + 15

if total_minutes >= 60:
    hours += 1
    total_minutes = total_minutes % 60

if hours >= 24:
    hours = 0

if total_minutes < 10:
    print(f"{hours}:0{total_minutes}")

else:
    print(f"{hours}:{total_minutes}")
