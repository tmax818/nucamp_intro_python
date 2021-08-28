
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


def validate_user(username, password):
    if len(username) < 10 and len(password) >= 5:
        return username, password
    else:
        print(
            "Username must be less than 10 characters and passwords must be at least 5!")
        return None, None
