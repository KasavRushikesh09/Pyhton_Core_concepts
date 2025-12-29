class AccountBalance(Exception):
    pass
balance = 5000
amount = 200

try:
    if amount > balance:
        raise AccountBalance("Insufficient Balance")
    balance -= amount
except AccountBalance as e:
    print(e)
else:
    print("withdrawel successfully..")
finally:
    print("Transaction completed..")