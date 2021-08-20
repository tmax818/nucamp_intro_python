# task 5
from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# task 2

print("          === Automated Teller Machine ===          ")
user = account.validate_name()

pin = account.validate_pin()
balance = 0

print(f"{user} has been registered with a starting balance of ${balance}")

# task 3

while True:
    user_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if user_to_validate == user and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
        continue

while True:
    atm_menu(user)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(user)
        break
