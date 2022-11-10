#!/usr/bin/env python3
# Created by: Katie G
# Created on: November 8th, 2022
# This program generates a random number, then uses a
# do...while loop to get the user number, uses a try...catch statement
# to check if the user input is an integer, then an if...then
# statement to check if the user's input is within the range of 0-9.
# the program then uses an if...then statement to check if the user guess
# is equal to the generated number - if so, uses a break statement to break
# out of the loop.
import random


# this function will generate a random number, then, while using a do...while loop,
# uses a try...catch statement and an if...then statement to check if the user
# guess is valid, then uses an if...then statement to check if the user guess
# is equal to the generated num - if so, uses a "break" statement to break
# out of the loop.
def main():
    # generates a random number from 0-9 and assigns it
    # to the random number variable.
    random_num = random.randint(0, 9)

    # the beginning of the do... while loop that the rest of
    # the program will be contained in.
    while True:
        # getting the user input.
        user_guess_as_string = input(
            "I am thinking of a number from 0-9. You will guess what it is please. "
        )
        # try...catch to make sure the user's input is valid.
        try:
            user_guess_as_int = int(user_guess_as_string)
            # if statememt to check if the user number is between 0 and 9.
            if user_guess_as_int >= 0 and user_guess_as_int <= 9:
                # if statement to check if the user guess is equal to the random num.
                if user_guess_as_int == random_num:
                    print("You guessed correctly! Well done!")
                    break
                else:
                    print("You have not guessed correctly. Try again.")
            else:
                print("Please enter a whole, positive number from 0-9.")
        except Exception:
            print("Please enter a valid integer from 0-9.")


if __name__ == "__main__":
    main()
