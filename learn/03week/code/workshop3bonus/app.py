from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register, validate_user

database = {'admin': 'password123'}
donations = []
authorized_user = ""

while True:

    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)

    user_input = input("Choose an option: ")

    if user_input == '1':
        username = input("Ender username: ").lower()
        password = input("Ender password: ")
        authorized_user = login(database, username, password)
    if user_input == '2':
        username = input("Ender username: ").lower()
        password = input("Ender password: ")
        username, password = validate_user(username, password)
        if authorized_user:
            database[username] = password
    if user_input == '3':
        if authorized_user:
            donation = donate(authorized_user)
            if donation:
                donations.append(donation)
        else:
            print("You are not logged in.")
        print()
    if user_input == '4':
        show_donations(donations)
    if user_input == '5':
        print("Leaving DonateMe...")
        break
