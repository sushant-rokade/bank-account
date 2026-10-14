class BankAccount:
    bank_name = "PyBank"
    MIN_BALANCE = 0.0
    def __init__(self,owner,balance,transactions=None):
        self.owner = owner
        if balance < self.MIN_BALANCE :
            raise ValueError("Lower than minimum balance")
        self.balance = balance
        self.transactions = []

    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(("deposit", amount, self.balance))
        return self.balance

    def withdraw(self, amount):
        if amount < BankAccount.MIN_BALANCE or amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdraw",amount, self.balance))
        return self.balance
    
    def summary(self):
        return f'{self.owner} . {self.balance:,.2f}' 
    
    def transfer_to(self, other, amount: float = 0.0):
        amt1 = self.balance
        amt2 = other.balance
        try:
            self.withdraw(amount)
            other.deposit(amount)
        except ValueError:
            # To ensure atomicity
            if self.balance != amt1:
                self.balance = amt1
                self.transactions.pop()
            raise ValueError("Transaction failed")
