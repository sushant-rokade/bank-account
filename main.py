from .account import BankAccount

def main():
    acc_holders = {}
    while True:
        print('\n1. Open Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Transactions\n6. Quit')
        ch = int(input("Enter choice: "))
        if ch == 1:
            owner = input("Enter owner name: ").strip().lower()
            balance = float(input("Enter balance: "))
            try:
                acc_holders[owner] = BankAccount(owner,balance)
            except ValueError as e:
                print(e)
        elif ch == 2:
            owner = input("Enter owner name: ").strip().lower()
            if owner not in acc_holders:
                print("No such accout")
            else:
                amount = input("Enter amount: ")
                try:
                    acc_holders[owner].deposit(amount)
                except ValueError as e:
                    print(e)
        elif ch == 3:
            owner = input("Enter owner name: ").strip().lower()
            if owner not in acc_holders:
                print("No such account")
            else:
                amount = input("Enter amount: ")
                try: 
                    acc_holders[owner].withdraw(amount)
                except ValueError as e:
                    print(e)
        elif ch == 4:
            sender = input("Enter sender name: ").strip().lower()
            receiver = input("Enter receiver name: ").strip().lower()
            if sender not in acc_holders and receiver not in acc_holders:
                print("No such account")
            else:
                amount = input("Enter amount: ")
                try:
                    acc_holders[sender].transfer_to(acc_holders[receiver],amount)
                except ValueError as e:
                    print(e)
        elif ch == 5:
            owner = input("Enter owner name: ").strip().lower()
            if owner not in acc_holders:
                print("No such account")
            else:
                print(acc_holders[owner].get_transactions_list())
        elif ch == 6:
            print("Thank you for coming")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()