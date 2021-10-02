# task 4


def show_balance(balance):
    print(f"Current Balance: ${balance}")


def deposit(balance):

    balance += amount
    return balance

# Bonus Task 3


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    while amount > balance:
        print("Where are you going to get that kind of money?")
        amount = float(input("Enter amount to withdraw: "))
    balance -= amount
    return balance


def logout(name):
    print(f"Goodbye {name}!")

# Bonus Task 1


def validate_name():
    name = input("Enter name to register: ")
    while len(name) < 1 or len(name) > 10:
        if len(name) < 1:
            print("You must enter a name")
            name = input("Enter name to register: ")
        if len(name) > 10:
            print("That name is too long!")
            name = input("Enter name to register: ")
    return name

# Bonus task 2


def validate_pin():
    pin = input("Enter PIN: ")
    while len(pin) != 4:
        print("PIN must contain 4 numbers")
        pin = input("Enter PIN: ")
    return pin


def validate_transaction(num):
    try:
        float(num)
    except NameError:
        print('please only use numbers')
    finally:
        return num
