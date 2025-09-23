class BankAccount(object):

    idNumber = 1
    
    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType =  accountType
        self.balance = balance

        self.accountNumber = BankAccount.idNumber
        BankAccount.idNumber += 1

        
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.file = open(self.filename, "a+")

    def depostMoney(self, amount):
        self.balance += amount
        self.file.seek(0,2)
        self.file.write("Deposit: " + str(amount) + " Final Balance: " + str(self.balance) + "\n")

    def withdrawMoney(self, amount):
        self.balance -= amount
        if self.balance < 0:
            amount += self.balance
            self.balance = 0

        self.file.seek(0,2)
        self.file.write("Withdraw: " + str(amount) + " Final Balance: " + str(self.balance) + "\n")

    def getBalance(self):
        return self.balance
    
    def getID(self):
        return self.accountNumber
    
    def getUsername(self):
        return self.name
    
    def getAccountType(self):
        return self.accountType
    
    def getTransactionHistory(self):
        self.file.seek(0)
        print("Transaction History: ")
        print(self.file.read())


def main():
    accounts = []

    for i in range(0, 10):
        name = "user" + str(i)
        accounts.append(BankAccount(name, "savings", 1000 * i))

    


main()
    

            