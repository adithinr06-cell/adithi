# Online Shopping Cart

# Product catalog
products = {
    1: ("T-Shirt", 500),
    2: ("Jeans", 1200),
    3: ("Shoes", 2000),
    4: ("Watch", 1500),
    5: ("Bag", 800)
}

cart = []
total = 0

def display_products():
    print("\n------ PRODUCT LIST ------")
    for key, value in products.items():
        print(f"{key}. {value[0]} - ₹{value[1]}")
    print("---------------------------")

while True:
    display_products()
    
    try:
        choice = int(input("Enter product number: "))
        
        if choice in products:
            quantity = int(input("Enter quantity: "))
            
            name, price = products[choice]
            cost = price * quantity
            
            cart.append((name, quantity, cost))
            total += cost
            
            print(f"{name} added to cart!")
        
        else:
            print("Invalid product choice!")
    
    except ValueError:
        print("Enter valid numbers only!")
        continue

    more = input("Do you want to add more items? (y/n): ")
    if more.lower() != 'y':
        break

# Apply Discount Logic
discount = 0

if total > 5000:
    discount = total * 0.20   # 20% discount
elif total > 3000:
    discount = total * 0.10   # 10% discount
elif total > 1000:
    discount = total * 0.05   # 5% discount

final_amount = total - discount

# Bill Display
print("\n------ SHOPPING BILL ------")
for item, qty, cost in cart:
    print(f"{item} x {qty} = ₹{cost}")

print("----------------------------")
print(f"Total Amount: ₹{total}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount to Pay: ₹{final_amount:.2f}")
print("Thank you for shopping! 🛍️")