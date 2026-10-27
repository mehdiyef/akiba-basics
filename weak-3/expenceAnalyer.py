print("======================== Function-Based Expense Analyzer ========================")

def add_expense(expenses,expense):
    expenses.append(expense)
    
def calculate_total(expenses):
    total=0
    
    for expense in expenses:
        total+=expense["amount"]
        
    return total


def calculate_by_catagory(expenses):
    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    return category_total

  
def largest_expense(expenses):
    largest=expenses[0]["amount"]
    largest_accomulator=expenses[0]
    for ex in range(1,len(expenses)):
        if expenses[ex]["amount"] > largest:
            largest_accomulator=expenses[ex]
    return largest_accomulator

def expense_above_threshold(expenses, threshold):
    expens_above_threshold=[]
    for expense in expenses:
        if expense["amount"] > threshold:
            expens_above_threshold.append(expense)
            
    return expens_above_threshold

def generate_spending_report(expenses):
    print("expense", "category", "amount", sep="                    ")
    for expense in expenses:
        print(expense["description"], expense["category"], expense["amount"], sep="                  ")
# expenses = [
#     {"description": "Lunch", "category": "Food", "amount": 150},
#     {"description": "Bus ticket", "category": "Transport", "amount": 50},
#     {"description": "Dinner", "category": "Food", "amount": 200},
#     {"description": "Notebook", "category": "Education", "amount": 120},
#     {"description": "Taxi", "category": "Transport", "amount": 100},
#     {"description": "Movie ticket", "category": "Entertainment", "amount": 250},
#     {"description": "Coffee", "category": "Food", "amount": 80},
#     {"description": "Medicine", "category": "Health", "amount": 300}
# ] 




def main():
    expenses=[]
    while True:
        print("\n========== Expense Analyzer ==========")
        print("1. Add an expense")
        print("2. Calculate total expenses")
        print("3. Calculate expenses by category")
        print("4. Find the largest expense")
        print("5. Find expenses above a threshold")
        print("6. Generate spending report")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                description = input("Enter expense description: ")
                category = input("Enter category: ")

                amount = float(input("Enter amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue


                add_expense(expenses,{
                    "description": description,
                    "category": category,
                    "amount": amount
                })
                print("Expense added successfully!")
            case "2":
                print("Total expenses:", calculate_total(expenses))

            case "3":
                totals = calculate_by_catagory(expenses)

                if not totals:
                    print("No expenses recorded.")
                else:
                    for category, total in totals.items():
                        print(f"{category}: {total}")

            case "4":
                if not expenses:
                    print("No expenses recorded.")
                else:
                    largest = largest_expense(expenses)
                    print("Largest expense:", largest["description"],",", largest["amount"])

            case "5":
       
                threshold = float(
                    input("Enter the threshold amount: ")
                )

                results = expense_above_threshold(
                    expenses, threshold
                )

                if not results:
                    print("No expenses above that threshold.")
                else:
                    generate_spending_report(results)                        

            case "6":
                if not expenses:
                    print("No expenses recorded.")
                else:
                    generate_spending_report(expenses)

            case "0":
                print("Exiting")
                break

            case _:
                print("Invalid choice. Please select 0-6.")


main()

