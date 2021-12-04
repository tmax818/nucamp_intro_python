import random

high_score = 0


def dice_game():

    global high_score

    while True:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        total = dice_1 + dice_2
        print(f"Current Hig Score: {high_score}")
        print("1) Roll Dice")
        print("2) Leave Game")
        roll = input("Enter your choice: ")

        if roll == '1':
            print(f"You roll a... {dice_1}")
            print(f"You roll a... {dice_2}")

            print(f"You have rolled a total of: {total}")
            if total > high_score:
                print("New high score!")
                high_score = total
        elif roll == '2':
            print("Goodbye!")
            break


dice_game()
