from account import BankAccount
user1 = None
try: 
    user1 = BankAccount('Sushant',90000)
except ValueError as e:
    print(e)
user2 = None
try: 
    user2 = BankAccount('Rohit',7000)
except ValueError as e:
    print(e)
user3 = None
try:
    user3 = BankAccount('Mukesh',80000)
except ValueError as e:
    print(e)
user4 = None
try:
    user4 = BankAccount('Sukesh',-1)
except ValueError as e:
    print(e)

print(user1.summary() if user1 != None else 'None')
print(user2.summary() if user2 != None else 'None')
print(user3.summary() if user3 != None else 'None')
print(user4.summary() if user4 != None else ('None'))

# Added Deposit
print("Deposit:",end=" ")
user1.deposit(5000)
print(user1.summary())
print("Withdraw:",end=" ")
user1.withdraw(2000)
print(user1.summary())
print("Withdraw more than deposit:",end=" ")
try:
    print(user1.withdraw(100000))
except ValueError as e:
    print(e,"(failed withdrawal).")

# Transaction
print("Transaction from user1 to user3")
user1.transfer_to(user3, 20000)
print(user1.summary())
print(user3.summary())

# Adding in vipul
print("Adding deposit in Vipul:",end=" ")
print(BankAccount('Vipul',40000).deposit(1000))

# self is reference to the current object, we can also use different name but 'self' is industry standard.

print("Validate amount by class BankAccount: ",end="")
print(BankAccount.validate_amount(100))
print("Validate amount by object: ",end="")
print(user1.validate_amount(100))
