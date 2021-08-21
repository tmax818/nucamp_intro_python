import random

high_score = 0


def dice_game():

    global high_score

    while True:

        print("Current High Score: ", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "2":
            print("Goodbye")
            break
        elif choice == "1":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            total = die1 + die2

            print("You roll a... ", die1)
            print("You roll a... ", die2)

            print("You have rolled a total of: ", total)

            if total > high_score:
                high_score = total
                print("New high score!")
            else:
                continue


dice_game()
