"""Program that simulates dice rolling. It may be useful in many RPG games
because you can simulate a throw many times as needed and also with a dice
with many walls as you want. Too final result you may add some extra points.
"""
import re
import random


def dice_roll():
    """Input must be in format: xDy+z or xDy-z or xDy
x = how many throws?
y = how many walls dice have?
z(optional) = how many points add to final result?
"""
    dice = input("Input valid dice: ")
    regex_dice = re.match(r'(?P<x>\d*)[dD](?P<y>\d+)(?P<a>[+-])?(?P<z>\d+)?', dice)
    if regex_dice:
        throws = regex_dice.group('x')
        walls = regex_dice.group('y')
        extra_points = regex_dice.group('z')
        operation = regex_dice.group('a')
        throws_list = []
        i = 0
        while i < int(throws):
            throw = random.randint(1, int(walls))
            throws_list.append(throw)
            i += 1
        print(f'All throws: { throws }')
        for count, i in enumerate(throws_list):
            print(count, f'throw: Sum = { i }')
        print(f'Walls: { walls }')
        if extra_points is not None:
            print(f'Extra points: { extra_points }')
            if operation == "+":
                result = sum(throws_list) + int(extra_points)
            else:
                result = sum(throws_list) - int(extra_points)
        else:
            print('Extra points: 0')
            result = sum(throws_list)
        return print('\33[52m' + '\33[30m' + f'SUM: { result }' + '\33[0m')


print(__doc__)
print(dice_roll.__doc__)
dice_roll()
