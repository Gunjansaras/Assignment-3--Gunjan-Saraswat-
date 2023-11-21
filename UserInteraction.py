from BussinessLogic import *
class Application:
    def showMainMenu(self):       
        bank = Bank()
        print(bank.makelist())       
        while True:
            choice = int(input('enter choice from 1.select account, 2.open account, 3.Exit; '))
            if choice == 1:
                accountno = int(input('enter the account number of the account that you want to search; '))
                print(bank.searchAccount(accountno, Account))
                showAccountMenu(accountno,bank) 
            elif choice == 2:
                #open account
                account_type = input('Enter the account type: ')
                accountno = int(input('Enter the account number: '))
                accountHoldername = input('Enter the Account Holder Name: ')
                rate_of_interest = int(input('Enter the rate of interest: '))
                current_balance = int(input('Enter the current balance of the account: '))
                print(bank.openAccount(account_type, accountno, accountHoldername, rate_of_interest, current_balance ))
            else:
                print('Exit')
                break

def showAccountMenu(accountno,bank):
    while True:            
        choice = int(input('Enter choice from 1.check balance, 2.deposit, 3.withdraw, 4.Exit account: '))
        if choice == 1:
            for account in bank.getlist():
                if account.getAccountNumber() == accountno:
                    print('The current balance of the account is', account.getCurrentBalance())
        elif choice ==2:
            money = int(input('enter the money to be deposited: '))
            bank.addDeposit(accountno,money)
            print(bank.getlist())
        elif choice == 3:
            account = bank.searchAccount(accountno, Account)
            account_type = account.getAccountType()
            money = int(input('enter the amount of money to be withdrawn; '))
            result = account.withdraw(money)
            if(result == 'Transaction Rejected'):
                print(result)
            else:
                print(result, 'withdrawn.')      
              
        else:
            print('Exiting the account')
            break

application = Application()
application.showMainMenu()