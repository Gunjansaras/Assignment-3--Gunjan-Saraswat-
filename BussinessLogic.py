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

class Bank(Account):
    def __init__(self):
        print('Welcome to the bank!')
        self.nested_list_of_Accounts = []
        self.new_account = None

    def makelist(self):
        for i in range(6):
            try:
                account_type = input('Enter Account Type (savings/checking): ').lower()
                accountno = int(input('Enter Account Number: '))
                name = input('Enter Account Holder Name: ')
                rate_of_interest = float(input('Enter rate of interest: '))
                current_balance = float(input('Enter the current balance of the account: '))
                
                if account_type not in ["savings", "checking"]:
                    print("Invalid account type. Skipping account creation.")
                    continue

                if current_balance < 0:
                    print("Invalid current balance. Skipping account creation.")
                    continue

                if account_type == "savings":
                    minimum_balance = float(input("Enter the minimum balance of the account: "))
                    if minimum_balance < 0:
                        print("Invalid minimum balance. Skipping account creation.")
                        continue
                    self.new_account = SavingsAccount(accountno, name, rate_of_interest, current_balance, minimum_balance)
                elif account_type == "checking":
                    overdrafts = float(input("Enter the overdraft limit of the account: "))
                    if overdrafts < 0:
                        print("Invalid overdraft limit. Skipping account creation.")
                        continue
                    self.new_account = CheckingAccount(accountno, name, rate_of_interest, current_balance, overdrafts)

                self.nested_list_of_Accounts.append(self.new_account)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def getlist(self):
        return self.nested_list_of_Accounts

    def searchAccount(self, accountno):
        for account in self.nested_list_of_Accounts:
            if account.getAccountNumber() == accountno:
                return account
        return None

    def openAccount(self, account_type, accountno, name, rate_of_interest, current_balance):
        try:
            if account_type.lower() not in ["savings", "checking"]:
                print("Invalid account type. Account not created.")
                return None

            if current_balance < 0:
                print("Invalid current balance. Account not created.")
                return None

            if account_type.lower() == "savings":
                minimum_balance = float(input("Enter the minimum balance of the account: "))
                if minimum_balance < 0:
                    print("Invalid minimum balance. Account not created.")
                    return None
                new_account = SavingsAccount(accountno, name, rate_of_interest, current_balance, minimum_balance)
            elif account_type.lower() == "checking":
                overdrafts = float(input("Enter the overdrafts of the account: "))
                if overdrafts < 0:
                    print("Invalid overdraft limit. Account not created.")
                    return None
                new_account = CheckingAccount(accountno, name, rate_of_interest, current_balance, overdrafts)
            else:
                print("Invalid account type. Account not created.")
                return None

            self.nested_list_of_Accounts.append(new_account)
            return self.nested_list_of_Accounts
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return None

    def addDeposit(self, account_number, money):
        for account in self.nested_list_of_Accounts:
            if account.getAccountNumber() == account_number:
                if money < 0:
                    print("Invalid deposit amount. Transaction not allowed.")
                    return False
                account.deposit(money)
                return True
        return False