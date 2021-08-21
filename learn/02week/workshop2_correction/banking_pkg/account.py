
balance = 0


def show_balance():
    print(f"Current Balance: ${balance}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    return balance


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    balance -= amount
    return balance


def logout(name):
    print(f"Goodbye {name}!")
