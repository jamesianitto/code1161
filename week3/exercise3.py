"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nwelcome to the guessing game!")
    print("A number between _ and _?")
    lowerBound = input("Enter a lower bound: ")
    lowerBound = int(lowerBound)
    upperBound = input("Enter an upper bound: ")
    print("OK the, a number between " + str(lowerBound) + " and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    while not guessed:
      try:
        guessedNumber = (input("guess a number: "))
        print("gussed {},".format(guessedNumber),) #comma?
        if gussedNumber == actualNumber:
          print("You got it!! It was {}".format(actualNumber))
          guessed = True
        elif guessedNumber < lowerBound or guessedNumber > upperBound:
          print("You're guessing out of bounds!")
        elif guessedNumber < actualNumber:
          print("Too low!")
        else:
          print("Too high!")
      return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()
