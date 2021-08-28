
menu_items = ["Login", "Register", "Donate", "Show Donations", "Exit"]

title_string = f"=== DonateMe Homepage ==="
menu_string = f""
divider = f"{'-' * 53}"

total_donations = 0

for i, v in enumerate(menu_items):
    menu_string += "|"
    menu_string += f" {i + 1}.   {v.ljust(15).rjust(5)}".center(25)
    if i % 2 != 0:
        menu_string += "|\n"
        menu_string += divider
        menu_string += "\n"


def show_homepage():
    print("\n\n")
    print(title_string.center(50))
    print(divider)
    print(menu_string)
    print(divider)


def donate(username):
    global total_donations
    while True:
        try:
            donation_amt = float(input("Enter amount to donate: "))
            break
        except ValueError:
            print("Please enter a number")
            continue

    if donation_amt <= 0:
        print("You're a cheapskate!!")
        return
    total_donations += donation_amt
    donation = f"{username} donated ${donation_amt}!"
    print("Thank you!")
    return donation


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations:
        for donation in donations:
            print(donation)
        print(f"Total = ${total_donations}")
    else:
        print("Currently, there are no donations.")
