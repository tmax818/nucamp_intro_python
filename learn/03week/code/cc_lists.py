import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Press enter to pick a card, or Q then enter to quit: ")
    if user_input == "Q":
        break

    random.shuffle(diamonds)
    print(diamonds)
    hand.append(diamonds.pop())
    print(hand)

if not diamonds:
    print("There are no more cards to pick.")
