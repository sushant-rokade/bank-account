class BankAccount:
    bank_name = "PyBank"
    MIN_BALANCE = 0.0
    total_accounts = 0
    
    def __init__(self,owner,balance,transactions=None):
        self.owner = owner
        if balance < self.MIN_BALANCE :
            raise ValueError("Lower than minimum balance")
        self.balance = balance
        self.transactions = []
        self.total_accounts += 1

    def deposit(self,amount: float = 0.0):
        amount = BankAccount.validate_amount(amount)
        self.balance += amount 
        self.transactions.append(("deposit", amount, self.balance))
        return self.balance

    def withdraw(self, amount: float = 0.0):
        amount = BankAccount.validate_amount(amount)
        if amount >= self.balance:
            raise ValueError("Amount is greater than bank balance")
        self.balance -= amount
        self.transactions.append(("withdraw",amount, self.balance))
        return self.balance
    
    def summary(self):
        return f'{self.owner} . {BankAccount.format_money(self.balance)}' 
    
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
        
    @staticmethod
    def validate_amount(amount):
        try:
            num = float(amount)
            if num <= 0:
                raise ValueError("amount must be greater than 0.")
            return num
        except ValueError:
            raise ValueError("amount consist another characters than digits.")

    @staticmethod
    def format_money(amount):
        return f'{amount:,.2f}'

    @staticmethod
    def is_valid_owner(name):
        name = name.strip()
        if len(name) < 2:
            raise ValueError("owner doesn't even have 2 characters.")
        for i in name.lower():
            if not (i>= 'a' and i<='z'):
                raise ValueError("owner is not valid")
            