class Account:
    def __init__(self, accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountnumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
        self._accountType = accountType
    def getAccountNumber(self):
        return self._accountnumber
    def getAccountHolderName(self):
        return self._accountHolderName
    def getRateOfInterest(self):
        return self._rateOfInterest
    def getCurrentBalance(self):
        return self._currentBalance
    def setAccountHolderName(self, newName):
        self._accountHolderName = newName
    def setRateOfInterest(self, newRateof_int):
        self._rateOfInterest = newRateof_int
    def deposit(self, money):
        self._currentBalance+=money
        return self._currentBalance
    def withdraw(self, money):
        self._currentBalance-=money
        return self._currentBalance
    def getAccountType(self):
        return self._accountType

class SavingsAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__('savings',accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._minimumBalance = minimumBalance
    def withdraw(self, withdrawnMoney):
        if self._currentBalance - withdrawnMoney < self._minimumBalance:
            return 'Transaction Rejected'
        else:
            self._currentBalance-=withdrawnMoney
            return withdrawnMoney

class CheckingAccount(Account):
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraft):
        super().__init__('checking',accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraft = overdraft
    def withdraw(self, withdrawnmoney):
        if withdrawnmoney > self._currentBalance + self._overdraft:
            return 'Transaction Rejected'
        else:
            self._currentBalance -= withdrawnmoney
            return withdrawnmoney

class Bank:
    def __init__(self):
        print('Welcome to the bank!')
        self.nested_list_of_Accounts = [] 
        self.new_account = None 
    def makelist(self):            
        for i in range(3 ):
            account_type = input('what is your account type? ')
            accountno = int(input('enter accountno; '))
            name = input('account holder name; ')
            rate_of_interest = int(input('enter rate of interest; '))
            Current_balance = int(input('enter the current balance of the account; '))  
            #accountlist = [account_type, accountno, name, rate_of_interest, Current_balance]
            if(account_type.lower() == "savings"):
                minimum_balance = int(input("enter the minimum balance of the account: "))
                self.new_account = SavingsAccount(accountno, name, rate_of_interest, Current_balance, minimum_balance)
            elif(account_type.lower() == "checking"):
                overdrafts = int(input("enter the overdrafts of the account: "))
                self.new_account = CheckingAccount(accountno, name, rate_of_interest, Current_balance,overdrafts)
            else:
                pass 
            self.nested_list_of_Accounts.append(self.new_account)
    def getlist(self):
        return self.nested_list_of_Accounts
    def searchAccount(self, accountno ):
        for account in self.nested_list_of_Accounts:
            if(account.getAccountNumber() == accountno):
                return account
    def openAccount(self, account_type, accountno, name, Rate_of_interest, currentBalance):
        if(account_type.lower() == "savings"):
            minimum_balance = int(input("enter the minimum balance of the account: "))
            self.new_account = SavingsAccount(accountno, name, Rate_of_interest, currentBalance, minimum_balance)
        elif(account_type.lower() == "checking"):
            overdrafts = int(input("enter the overdrafts of the account: "))
            self.new_account = CheckingAccount(accountno, name, Rate_of_interest, currentBalance,overdrafts)
        else:
            pass 
        self.nested_list_of_Accounts.append(self.new_account)
        return self.nested_list_of_Accounts
    def addDeposit(self, account_number, money):
        for account in self.nested_list_of_Accounts:
            if(account.getAccountNumber() == account_number):
                account.deposit(money)
