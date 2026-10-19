
print("========================== bank transaction processor ==========================")

history = []
def deposit_money(balance, amount):
    if amount < 0:
        return None

    return balance + amount


def withdraw_money(balance, amount):
    if amount < 0 or amount > balance:
        return None

    return balance - amount


def current_money(balance):
    return balance


def record_transaction(balance, amount, action):
    if action == "deposit":
        new_balance = deposit_money(balance, amount)

    elif action == "withdraw":
        new_balance = withdraw_money(balance, amount)

    else:
        return balance

    if new_balance is None:
        print("Invalid transaction!")
        return balance

    history.append({
        "type": action,
        "amount": amount,
        "balance": new_balance
    })

    return new_balance


def transaction_summery():
    balance = 0

    balance = record_transaction(balance, 1200, "deposit")
    balance = record_transaction(balance, 1200, "deposit")
    balance = record_transaction(balance, 1600, "withdraw")

    for h in history:
        print("Type:", h["type"])
        print("Amount:", h["amount"])
        print("Balance:", h["balance"])
        print("--------------------")

    print("Current balance:", current_money(balance))


transaction_summery()
