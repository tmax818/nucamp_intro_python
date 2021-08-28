
def login(database, username, password):
    if username in database.keys() and database[username] == password:
        print(f"\nWelcome back {username}!")
        return username
    elif username in database.keys() and database[username] != password:
        print("invalid credentials")
        return ""
    else:
        print("who the hell are you?")
        return ""


def register(database, username):
    if username in database.keys():
        print(f"{username} already registered!")
        return ""
    else:
        print(f"Username {username} registered!")
        return username
