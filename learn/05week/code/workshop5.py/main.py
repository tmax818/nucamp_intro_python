import random


def guess_random_number(tries, start, stop):
    piv = random.randint(start, stop + 1)
    print(piv)

    while tries != 0:
        print(tries)
        user_guess = input("Guess a number btwn 0 and 10: ")


guess_random_number(2, 0, 100)
