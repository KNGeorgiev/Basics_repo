total_tickets = 0
student = 0
standard = 0
kid = 0
movie_name = input()

while movie_name != "Finish":
    capacity = int(input())
    ticket_type = input()
    current_ticket_num = 0

    while ticket_type != "End":
        current_ticket_num += 1
        total_tickets += 1

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1

        if current_ticket_num == capacity:
            break

        ticket_type = input()
    print(f"{movie_name} - {current_ticket_num / capacity * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{student / total_tickets * 100:.2f}% student tickets.")
print(f"{standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid / total_tickets * 100:.2f}% kids tickets.")