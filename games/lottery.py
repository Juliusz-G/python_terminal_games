"""Lottery simulator. Users have to choose six numbers and then its go through
the 'control' and if verification will passed then program draws randomly
another six numbers. Then two list of numbers (user list and random list) are
compared. At the end program prints how many numbers user have hit.
"""
import random


def lottery():
    """Input must be in the right format: 1 12 43 4 32 14
    Rules:
    - Numbers must be separated by spaces
    - There must be six numbers
    - Numbers must be from 1 to 49
    - Numbers must be unique
    """
    try:
        user_numbers = [int(number) for number in input("Enter multiple value: ").split()]
        if len(user_numbers) == 6:
            if len(user_numbers) == len(set(user_numbers)):
                for number in user_numbers:
                    if number not in range(1, 50):
                        print("Number is not in range 1 to 49. Try again!")
                        return lottery()
            else:
                print("Numbers must be unique. Try again!")
                return lottery()
        else:
            print("Input numbers again! You have to choose 6 numbers!")
            return lottery()
        user_numbers.sort()
        print(f"Your numbers: { user_numbers }")
        drawn_list = []
        while len(drawn_list) < 6:
            drawn_number = random.randint(1, 49)
            if drawn_number not in drawn_list:
                drawn_list.append(drawn_number)
            else:
                pass
        drawn_list.sort()
        print(f"Drawn numbers: { drawn_list }")
        result = list(set(user_numbers).intersection(set(drawn_list)))
        print(f"You hit: { len(result) } numbers.")
    except ValueError:
        print("Its not a number! Try again!")
        return lottery()
    except KeyboardInterrupt:
        print("\33[4m" + "\nThank you!!!" + "\33[0m")


print(__doc__)
print(lottery.__doc__)
lottery()
