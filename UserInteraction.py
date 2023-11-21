from BussinessLogic import *
class Application:
    def showMainMenu(self):
        bank = Bank()
        print(bank.makelist())
        while True:
            try:
                choice = int(input('Enter choice from 1.select account, 2.open account, 3.Exit: '))
                if choice == 1:
                    accountno = int(input('Enter the account number of the account that you want to search: '))
                    print(bank.searchAccount(accountno))
                    showAccountMenu(accountno, bank)
                elif choice == 2:
                    # open account
                    account_type = input('Enter the account type (savings/checking): ')
                    accountno = int(input('Enter the account number: '))
                    accountHoldername = input('Enter the Account Holder Name: ')
                    rate_of_interest = float(input('Enter the rate of interest: '))
                    current_balance = float(input('Enter the current balance of the account: '))
                    print(bank.openAccount(account_type, accountno, accountHoldername, rate_of_interest, current_balance))
                elif choice == 3:
                    print('Exit')
                    break
                else:
                    print('Invalid choice. Please enter 1, 2, or 3.')
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def showAccountMenu(accountno, bank):
    while True:
        try:
            choice = int(input('Enter choice from 1.check balance, 2.deposit, 3.withdraw, 4.Exit account: '))
            if choice == 1:
                for account in bank.getlist():
                    if account.getAccountNumber() == accountno:
                        print('The current balance of the account is', account.getCurrentBalance())
            elif choice == 2:
                money = float(input('Enter the money to be deposited: '))
                if money < 0:
                    print("Invalid deposit amount. Transaction not allowed.")
                else:
                    bank.addDeposit(accountno, money)
                    print(bank.getlist())
            elif choice == 3:
                account = bank.searchAccount(accountno)
                if account:
                    account_type = account.getAccountType()
                    money = float(input('Enter the amount of money to be withdrawn: '))
                    if money < 0:
                        print("Invalid withdrawal amount. Transaction not allowed.")
                    else:
                        result = account.withdraw(money)
                        if isinstance(result, str):
                            print(result)
                        else:
                            print(result, 'withdrawn.')
                else:
                    print("Account not found.")
            elif choice == 4:
                print('Exiting the account')
                break
            else:
                print('Invalid choice. Please enter 1, 2, 3, or 4.')
        except ValueError:
            print("Invalid input. Please enter a valid number.")

application = Application()
application.showMainMenu()