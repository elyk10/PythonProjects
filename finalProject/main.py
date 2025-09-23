class BankAccount(object):

    idNumber = 1
    
    def __init__(self, name, accountType, balance = 0):
        self.name = name
        self.accountType =  accountType
        self.balance = balance

        self.accountNumber = BankAccount.idNumber
        BankAccount.idNumber += 1

        
        self.filename = str(self.accountNumber) + "_" + self.accountType + "_" + self.name + ".txt"
        self.file = open(self.filename, "w+")

    def depostMoney(self, amount):
        self.balance += amount
        self.file.seek(0,2)
        self.file.write("Deposit: " + str(amount) + " Final Balance: " + str(self.balance) + "\n")

    def withdrawMoney(self, amount):
        self.balance -= amount
        tempAmount = amount
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
    accounts = [BankAccount("Kyle", "Chequeing", 923)]

    for i in range(0, 10):
        name = "user" + str(i)
        accounts.append(BankAccount(name, "savings", 1000 * i))

    loop = True

    while loop:
        addAccount = input("Would you like to add an account (yes/no)?")
        if addAccount == "yes":
            name = input("What is the name on the account?")
            accountType = input("What is the account type?")
            balance = float(input("What is the intial balance?"))
            accounts.append(BankAccount(name, accountType, balance))
        
        else:
            loop = False

    accounts[1].withdrawMoney(3000)
    accounts[1].depostMoney(2)
    accounts[0].depostMoney(3)

    for i in accounts:
        print(i.accountNumber)
        print(i.balance)
        i.getTransactionHistory()
    


main()
    

            