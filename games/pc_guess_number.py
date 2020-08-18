"""Simple guessing game. Program will guess
a number in maximum 10 steps. User have to
enter a number form 1 to 1000 and response
correctly to program commands.
"""


def pc_guess_number():
    """Simple algorithm that cuts (narrows) a field to half, and repeats till its guessed a user number."""
    user_number = list(range(1, 1001))
    min_number = user_number[0]
    max_number = user_number[999]
    print("Think about a number and I will guessed it in max 10 steps!\n".upper())
    for i in range(0, 10):
        guess = int((max_number - min_number) / 2) + min_number
        print(f"~~~~~I think its : { guess }~~~~~".upper())
        try:
            answer = input("""
            1 : Less
            2 : More
            3 : Guessed
            Your input (1, 2 or 3): """)
            if int(answer) == 1:
                max_number = guess
            elif int(answer) == 2:
                min_number = guess
            elif int(answer) == 3:
                return print("Haha I know it!!!".upper())
            elif int(answer) is not (1, 2, 3):
                print("Don't cheat!")
                return pc_guess_number()
        except ValueError:
            print("You should put a number from 1 to 3!!!")
            return pc_guess_number()


print(__doc__)
print(pc_guess_number.__doc__)
pc_guess_number()
