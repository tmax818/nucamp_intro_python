
class User:
    def __init__(self, name, pin, password) -> None:
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):

    balance = 0

    def __init__(self, name, pin, password) -> None:
        super().__init__(name, pin, password)

    def show_balance(self):
        print(f"{self.name} has an account balance of: {self.balance}")

    def withdraw(self, amount):
        if (type(amount) is not int or type(amount) is not float):
            return
        if amount <= 0:
            print("only positive amounts are allowed.")
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    """
            ----------Task Five ----------
        Create two more methods for the BankUser class:
            * transfer_money
                - Transfers money to another User if
                - correct PIN is given for transferring User
            * request_money
                - Will ask for the PIN of the User being requested for money.
                - If credentials are correct,
                    - Will ask for and validate the password of the User requesting money as well,
                    - Then complete the transfer, removing money from one account and adding the same amount to the other.
    """

    def transfer_money(self, user, amount):
        print("You are transferring $" + str(amount), "to", user.name)
        print("Authentication required")
        pincode = int(input("Enter your PIN: "))
        if pincode != self.pin:
            print("Invalid PIN. Transaction canceled.")
            return False
        print("Transfer authorized")
        print("Transferring $" + str(amount) + " to " + user.name)
        self.balance -= amount
        user.balance += amount

        return True

    def request_money(self, user, amount):
        print("You are requesting $" +
              str(amount), "from", user.name)
        print("User authentication is required...")

        pin = int(input("Enter " + user.name + "'s PIN: "))
        if pin != user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False

        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction canceled.")
            return False

        print("Request authorized")
        print(user.name + " sent $" + str(amount))

        user.balance -= amount
        self.balance += amount

        return True


user1 = BankUser('bob', 1234, 'password')
user2 = BankUser('alice', 1234, 'password')
