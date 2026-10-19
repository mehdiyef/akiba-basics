print("========================== bank transaction processor==========================   ")


def deposit_money(amount):
    if not amount < 0:
        balance+=amount
        return balance
    return None
def withdraw_money(amount):
    balance -= amount
    return balance

def current_money():
    return balance
history=[]
balance=0
def record_transaction(balance, action):

    if action == "deposit":
        history.append({
            "type":action,
            "amount":balance,
            "balance":deposit_money(balance)
        })
    if action == "withdraw":
        history.append({
            "type":action,
            "amount":balance,
            "balance":withdraw_money(balance)
        })


record_transaction(1200, "deposit")
record_transaction(1200, "deposit")
record_transaction(1600, "withdraw")

for h in history:
    print(h["type"])
    print(h["amount"])
    print(h["balance"])
    
print(current_money())