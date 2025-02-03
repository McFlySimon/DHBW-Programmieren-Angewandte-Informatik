def calculate_ticket_price(age, is_student, is_senior):
    base_price = 20
    discount = 0
    
    if is_senior:
        discount = 0.3
    elif is_student and age < 30:
        discount = 0.2
    
    final_price = base_price * (1 - discount)
    return final_price


age = int(input("Geben Sie Ihr Alter ein: "))
is_student = input("Sind Sie Student? (ja/nein): ").strip().lower() == "ja"
is_senior = input("Sind Sie Senior? (ja/nein): ").strip().lower() == "ja"

# Ticketpreis
price = calculate_ticket_price(age, is_student, is_senior)
print(f"Der Ticketpreis beträgt: {price:.2f} Euro")
