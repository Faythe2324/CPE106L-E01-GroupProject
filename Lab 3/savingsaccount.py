class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE= 0.02    # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        """Returns the string rep."""
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def deposit(self, amount):
        """If valid, adds it to balance; else error message."""
        if amount < 0:
            return "Amount must be >= 0"
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
