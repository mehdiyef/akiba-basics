print("======================= Inventory Stock Controller ====================")


def add_product(products):
    products_name = []
    for p in products:
        products_name.append(p["name"])

    while True:
        product_name = input("enter the name of the product: ")
        if not product_name:
            print("name can't be empity")
            continue
        if product_name in products_name:
            print("there is a duplicated name")
            continue
        break
    product_price = float(input("enter the price of the product: "))
    product_quntity = int(input("enter the quntity of the product: "))
    products.append({
        "name": product_name,
        "price": product_price,
        "quantity": product_quntity
    })

    print("Successfully added!")


def searc_product(products):
    search_product = input("Enter the product to be searched: ")
    for product in products:
        if product["name"] == search_product:
            print("Search found!")
            break
        return product


def update_price(products):
    product_to_be_update = input("Enter the name of the product to be update: ")
    for product in products:
        if product["name"] == product_to_be_update:
            new_price = float(input("Enter the new price: "))
            product["price"] = new_price

    print("Successfully updated the price")


def update_stock(products):
    product_to_be_update = input("Enter the name of the product to be update: ")
    for product in products:
        if product["name"] == product_to_be_update:
            stock_updated = int(input("Enter the stock updated: "))
            product["quantity"] = stock_updated
    print("Successfully updated the stock")


def sell_product(products):
    name_product = input("Enter the name of the product you wanna sell: ")
    quantity_to_buy = int(input("Enter the quantity  also: "))

    for product in products:
        if product["name"] == name_product:
            product["quantity"] -= quantity_to_buy
    print(f"Successfully bought {name_product}")


def calculate_total(products):
    total = 0
    for product in products:
        total += (product["price"] * product["quantity"])

    return total


def low_stock(products):
    low_stocks = []
    for product in products:
        if product["quantity"] <= 3:
            low_stocks.append(product)
    return low_stocks


def show_products(products):
    print("========================================= This is your stocks ==================================")
    print(f"name", "price", "quantity", sep="                   ")
    print("----------------------------------------------------------------------------------------------")
    for product in products:
        print(product["name"], product["price"], product["quantity"], sep="                   ")
    print("======================================================================================")


def main():
    products = [{'name': 'shoe', 'price': 123.0, 'quantity': 4}, {'name': 't-shirt', 'price': 32.0, 'quantity': 4},
                {'name': 'glove', 'price': 89.0, 'quantity': 3}, {'name': 'boxer', 'price': 56.0, 'quantity': 8}]

    while True:
        print(
            "Enter \n1. To add a product \n2. To search a product \n3. To update product price \n4. To increase stock \n5. sell product \n5. Calculate total inventory \n6. To generate low stock \n7. To show all products \n8. To exit ")
        choice = input("Enter your choice: ")

        match (choice):
            case "1":
                add_product(products)
            case "2":
                print(
                    f"name: {searc_product(products)["name"]} \nprice: {searc_product(products)["price"]} \nquantity: {searc_product(products)["quantity"]}")
            case "3":
                update_price(products)
            case "4":
                update_stock(products)
            case "5":
                print("total inventory: ", calculate_total(products))
            case "6":
                if not low_stock(products):
                    print("There is enough stock on the store.")

                else:
                    show_products(low_stock(products))
            case "7":
                show_products(products)
            case "8":
                print("Exitting..........")
                break
            case _:

                print("invalid input, please try again")


main()
