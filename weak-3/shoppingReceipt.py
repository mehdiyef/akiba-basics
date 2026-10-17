print("===================Welcome to the Shopping Receipt Generator!=====================")

# def sub_total_each_item(price, quantity: number):
#     return price * quantity

def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        subtotal += item['price'] * item['quantity']
    return subtotal

def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.1      
    elif subtotal > 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    refined_total = subtotal - discount
    tax = calculate_tax(refined_total, tax_rate)
    total = refined_total + tax

    receipt = {
        'items': items,
        'subtotal': subtotal,
        'discount': discount,
        'tax': tax,
        'total': total
    }
    return receipt


items = []
while True:
    choice = (input("Enter \n1.to add items\n2.to generate receipt\n3.to exit\n "))
    match choice:
        case "1":
        
            item_name = input("Enter item name: ")
            if item_name.lower() == 'done':
                break
            
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            if item_price < 0 or item_quantity < 0:
                print("Price and quantity must be non-negative. Please try again.")
                continue
            
            
            items.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
            print("\nItems added successfully!\n")
            
        case "2":
            tax_rate = 0.03  # let 3% be tax rate
            receipt = generate_receipt(items, tax_rate)
            print("\n==================== Receipt ====================")
            print("name", "price", "quantity", sep="           ")
            for item in receipt['items']:
                print(f"{item['name']}" ,f"${item['price']}"  ,f"{item['quantity']}", sep="           ")
                
                
            print("\nsubtotal: ", f"${receipt['subtotal']:.2f}")
            print("discount: ", f"${receipt['discount']:.2f}")
            print("tax: ", f"${receipt['tax']:.2f}")
            print("Total: ", f"${receipt['total']:.2f}")
            print("=================================================\n")
            
            
        case "3":
            print("Thank you for shopping with us!")
            break
        case _:
            print("Invalid choice. Please try again.")
