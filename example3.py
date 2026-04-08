# Hotel Menu Program

def display_menu():
    print("\n------ HOTEL MENU ------")
    print("1. Masala Dosa      - ₹50")
    print("2. Idli             - ₹30")
    print("3. Veg Biryani      - ₹120")
    print("4. Paneer Butter Masala - ₹150")
    print("5. Chapati          - ₹20")
    print("6. Gulab Jamun      - ₹40")
    print("-------------------------")

# Menu dictionary
menu = {
    1: ("Masala Dosa", 50),
    2: ("Idli", 30),
    3: ("Veg Biryani", 120),
    4: ("Paneer Butter Masala", 150),
    5: ("Chapati", 20),
    6: ("Gulab Jamun", 40)
}

total_bill = 0
order_list = []

while True:
    display_menu()
    
    try:
        choice = int(input("Enter item number to order: "))
        
        if choice in menu:
            quantity = int(input("Enter quantity: "))
            
            item_name, price = menu[choice]
            cost = price * quantity
            
            total_bill += cost
            order_list.append((item_name, quantity, cost))
            
            print(f"{item_name} added to order!")
        
        else:
            print("Invalid choice! Please select from menu.")
    
    except ValueError:
        print("Please enter valid numbers!")
        continue

    more = input("Do you want to order more? (y/n): ")
    if more.lower() != 'y':
        break

# Final Bill
print("\n------ FINAL BILL ------")
for item, qty, cost in order_list:
    print(f"{item} x {qty} = ₹{cost}")

print("-------------------------")
print(f"Total Amount: ₹{total_bill}")
print("Thank you! Visit again 😊")