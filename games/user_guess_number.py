"""Simple guessing game. User have to guess a number
from 1 to 100. if its number is too big or too small
the program will inform about that and the user will
have another chance to guess it.
"""
import random


def guess_number():
    """While random number is not guessed loop will continue."""
    print("Try to guess a number from 1 to 100")
    print("-----------------------------------")
    while True:
        try:
            random_number = random.randint(1, 101)
            guess = 0
            while guess != random_number:
                guess = int(input("Input a number: "))
                if guess == random_number:
                    return print("Guessed!")
                elif guess > random_number:
                    print("Too much!")
                elif guess < random_number:
                    print("Not enough!")
        except ValueError:
            print("It's not a number!")


print(__doc__)
print(guess_number.__doc__)
guess_number()
