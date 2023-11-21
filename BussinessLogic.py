class Account:                      #Account class created 
    def __init__(self, accountType, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self._accountnumber = accountNumber
        self._accountHolderName = accountHolderName
        self._rateOfInterest = rateOfInterest
        self._currentBalance = currentBalance
        self._accountType = accountType
    def getAccountNumber(self):    #Account number accessor 
        return self._accountnumber
    def getAccountHolderName(self):  #Account Holder Name accessor 
        return self._accountHolderName
    def getRateOfInterest(self):   #Rate Of interest accessor 
        return self._rateOfInterest
    def getCurrentBalance(self):  #Current balance accessor 
        return self._currentBalance
    def setAccountHolderName(self, newName):   #Account Holder Name accessor 
        self._accountHolderName = newName
    def setRateOfInterest(self, newRateof_int):  #Rate of interest accessor 
        self._rateOfInterest = newRateof_int
    def deposit(self, money):      #deposit money
        self._currentBalance+=money
        return self._currentBalance
    def withdraw(self, money):     #withdraw money
        self._currentBalance-=money
        return self._currentBalance
    def getAccountType(self):      #Account Type money
        return self._accountType

class SavingsAccount(Account):      #HAS-A relationship
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, minimumBalance):
        super().__init__('savings',accountNumber, accountHolderName, rateOfInterest, currentBalance)    
        self._minimumBalance = minimumBalance
    def withdraw(self, withdrawnMoney):
        if self._currentBalance - withdrawnMoney < self._minimumBalance:
            return 'Transaction Rejected'
        else:
            self._currentBalance-=withdrawnMoney
            return withdrawnMoney

class CheckingAccount(Account):   #HAS-A relationship
    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraft):
        super().__init__('checking',accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self._overdraft = overdraft
    def withdraw(self, withdrawnmoney):
        if withdrawnmoney > self._currentBalance + self._overdraft:
            return 'Transaction Rejected'
        else:
            self._currentBalance -= withdrawnmoney
            return withdrawnmoney

class Bank(Account):            #HAS-A relationship
    def __init__(self):
        print('Welcome to the bank!')
        self.nested_list_of_Accounts = []
        self.new_account = None
    def makelist(self):
        try:                       #exception handling 
            for i in range(6):
                account_type = input('Enter Account Type: ')
                accountno = int(input('Enter Account Number: '))
                name = input('Enter Account Holder Name: ')
                rate_of_interest = int(input('Enter rate of interest: '))
                Current_balance = int(input('Enter the current balance of the account: '))  
                if(account_type.lower() == "savings"):
                    minimum_balance = int(input("Enter the minimum balance of the account: "))
                    self.new_account = SavingsAccount(accountno, name, rate_of_interest, Current_balance, minimum_balance)
                
                elif(account_type.lower() == "checking"):
                    overdrafts = int(input("Enter the overdraft limit of the account: "))
                    self.new_account = CheckingAccount(accountno, name, rate_of_interest, Current_balance,overdrafts)
            
                else:
                    return None        
            self.nested_list_of_Accounts.append(self.new_account)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
    def getlist(self):
        return self.nested_list_of_Accounts
    
    def searchAccount(self, accountno):
        for account in self.nested_list_of_Accounts:            
            if(account.getAccountNumber() == accountno):
                return account
        return None 
    
    def openAccount(self, account_type, accountno, name, Rate_of_interest, currentBalance):
        try:
            if(account_type == "savings"):
                minimum_balance = int(input("enter the minimum balance of the account: "))
                new_account = SavingsAccount(accountno, name, Rate_of_interest, currentBalance, minimum_balance)
        
            elif(account_type == "checking"):
                overdrafts = int(input("enter the overdrafts of the account: "))
                new_account = CheckingAccount(accountno, name, Rate_of_interest, currentBalance,overdrafts)

            else:
                return None 
        
            self.nested_list_of_Accounts.append(new_account)
            return self.nested_list_of_Accounts
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None
    
    def addDeposit(self, account_number, money):
        for account in self.nested_list_of_Accounts:
            if(account.getAccountNumber == account_number):
                account.deposit(money)
                return  True
        return False
