input()


def input_field(title="", blank_allowed=True, return_type="string"):

    def print_empty_error():
        print(f"The value you entered {input_value} is empty.\n"
              "Please try again...")

    def print_value_error():
        print(f"The value you entered {input_value} isn't a(n)",
              "{return_type}.\n",
              "Please try again...")

    def cast_value(input_value):
        print("return_type.lower():", return_type.lower())
        if return_type.lower() == "integer":
            if input_value:
                value = int(input_value)
            else:
                value = int(0)
        elif return_type.lower() == "float":
            if input_value:
                value = float(input_value)
            else:
                value = float(0)
        else:
            value = input_value

        return value

    # Start input loop
    while True:
        input_value = input(title)
        # Check input is integer
        try:
            if blank_allowed:
                if input_value:
                    print("Input_value:", input_value)
                    return cast_value(input_value)
            else:
                print_empty_error()
        except ValueError:
            print_value_error()


def menu():
    money = int(5000)
    money = float(money)
    # print the options you have
    print("Welcome to the Python Bank System")
    print(" ")
    print("Your Transaction Options Are:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1) Deposit Money")
    print("2) Withdraw Money")
    print("3) Check Balance")
    print("4) Quit Python Bank System.pyw")
    print()

    return input_field(title="Choose your option: ",
                       blank_allowed=True,
                       return_type="integer")


# Here is the deposit part.... This is where the user inputs the amount
# of money they wish to deposit into their account.
def deposit(money):
    global balance
    deposit = input_field(title="How much: $",
                       blank_allowed=True,
                       return_type="float")
    if deposit <= money:
        balance = balance + 1
        money = money - deposit
        money = float(money)
        deposit = deposit * .1
        deposit = float(deposit)
        balance = deposit + balance
        balance = float(balance)
        print("You've successfully deposited $", deposit, "into your account.")
        print
        bank_balance(balance)
        return balance


# This is where the user inputs the amount of money they wish to withdraw from
# their account. Currently not programmed in as of yet.
def withdrawl(balance, money):
    print("Entered", input_integer("Enter amount:"))
    print("Sorry, but this function is currently under construction!")
    return


# This is an obvious one, this is where you check your balance.
def bank_balance(balance):
    print("Balance: $", balance)
    return balance


# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
balance = 0
balance = float(balance)
money = 5000
money = float(money)
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        deposit = deposit(money)
    elif choice == 2:
        withdraw = withdrawl(balance, money)
    elif choice == 3:
        balance = bank_balance(balance)
    elif choice == 4:
        loop = 0
    print("Thank-You for stopping by the bank!")
# END OF THE PROGRAM
