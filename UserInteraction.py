from BussinessLogic import *
class Application:
    def showMainMenu(self):       
        bank = Bank()
        print(bank.makelist())          
        
        while True:
            choice = int(input('enter choice from 1.select account, 2.open account, 3.Exit; '))
            if choice == 1:
                accountno = int(input('enter the account number of the account that you want to search; '))
                print(bank.searchAccount(accountno))
                showAccountMenu(accountno,bank) 
            elif choice == 2:
                #open account
                account_type = input('enter the account type: ')
                accountno = int(input('enter the account number; '))
                accountHoldername = input('enter the account Holder name; ')
                rate_of_interest = int(input('enter the rate of interest; '))
                current_balance = int(input('enter the current balance of the account; '))
                print(bank.openAccount(account_type, accountno, accountHoldername, rate_of_interest, current_balance ))
            else:
                print('Exit')
                break