class Menu:
    def __str__(self):
        # print the options you have
        return """\n
Welcome to the Python Bank System

Your Transaction Options Are:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Deposit Money
2) Withdraw Money
3) Check Balance
4) Quit Python Bank System
"""

    def choice(self):
        choice = input("Choose your option: ")
        try:
            choice = int(choice)
            if not (1 <= choice <= 4):
                raise ValueError
        except ValueError:
            print("Your entry must be 1, 2, 3 or 4")
        return choice


class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        return self.balance


# def menu():
#     money = int(5000)
#     money = float(money)


# Here is the deposit part.... This is where the user inputs the amount
# of money they wish to deposit into their account.
# def deposit(money):
#     global balance
#     deposit = input("How much: $")
#     deposit = float(deposit)
#     if deposit <= money:
#         balance = balance + 1
#         money = money - deposit
#         money = float(money)
#         deposit = deposit * .1
#         deposit = float(deposit)
#         balance = deposit + balance
#         balance = float(balance)
#         print("You've successfully deposited $", deposit, "into your account.")
#         bank_balance(balance)
#         return balance


# This is where the user inputs the amount of money they wish to withdraw
# from their account. Currently not programmed in as of yet.
# def withdrawl(balance, money):
#     print("Sorry, but this function is currently under construction!")
#     return


# This is an obvious one, this is where you check your balance.
# def bank_balance(balance):
#     print("Balance: $", balance)
#     return balance


# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
menu = Menu()
account = Account(balance=0.00)

# money = 5000
# money = float(money)
# loop = 1

choice = 0
while choice != 4:
    print(menu)
    choice = menu.choice()
    if choice == 1:
        print("1")
        # deposit = deposit(money)
    elif choice == 2:
        print("2")
        # withdraw = withdrawl(balance, money)
    elif choice == 3:
        print("Your account balance is:", account.show_balance())
    elif choice == 4:
        print("4")
    print("Thank-You for stopping by the bank!")


#END OF THE PROGRAM
