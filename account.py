class BankAccount:
    bank_name = "PyBank"
    MIN_BALANCE = 0.0
    def __init__(self,owner,balance,transactions=None):
        self.owner = owner
        if balance < self.MIN_BALANCE :
            raise ValueError("Lower than minimum balance")
        self.balance = balance
        self.transactions = []
