#!/usr/bin/env python

import random


def getInput():
    """get user input for the number of dice and the number sides of dice.

    :returns tuple of # of dice and sides

    """
    while True:
        rawDice = input("enter number of dice and number of sides: ")
        dice = rawDice.strip(" ")
        delim = int(dice.find(" "))
        if delim == -1:
            print("invalid format: input = <number_of_dice> <number_of_sides>")
        else:
            break
    numberDice = int(dice[:delim])
    sidesDice = int(dice[delim + 1:])
    return (numberDice, sidesDice)


def main():
    """Main function that calculates dice
    """
    sum = 0
    numberDice, sidesDice = getInput()
    for i in range(1, numberDice + 1):
        dice = random.randint(1, sidesDice)
        sum += dice
        print(dice)

    print(f"sum = {sum}")


if __name__ == "__main__":
    while True:
        main()
