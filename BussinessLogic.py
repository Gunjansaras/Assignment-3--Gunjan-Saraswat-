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