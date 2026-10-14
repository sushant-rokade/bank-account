from account import BankAccount

def print_user_data(account):
    if(account!=None):
        print(account.owner," ",account.balance)
    else:
        print("Invalid Account")

user1 = None
try: 
    user1 = BankAccount('Sushant',9090099)
except ValueError as e:
    print(e)
user2 = None
try: 
    user2 = BankAccount('Rohit',700000)
except ValueError as e:
    print(e)
user3 = None
try:
    user3 = BankAccount('Mukesh',80000)
except ValueError as e:
    print(e)
user4 = None
try:
    user4 = BankAccount('Mukesh',-1)
except ValueError as e:
    print(e)


print_user_data(user1)
print_user_data(user2)
print_user_data(user3)
print_user_data(user4)

print("\n Removing balance 5000 from Mukesh ")
if(user4 != None):
    user4.balance -= 5000

print_user_data(user1)
print_user_data(user2)
print_user_data(user3)