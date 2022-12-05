# OBJECTIVE:
# like GuessTheNumber, but player player has to guess
# step one. computer generates number
# while loop for user to try his guess, if correct you win!
# if wrong, go to next guess or lose!
#
# should probably add validation


import random
import time

def generate_number():
    print("generating number beep boop")
    target = random.randint(1, 10)
    time.sleep(2)
    return target

def user_guesser():
        guessedNumber = int(input("Guess what number I am thinking of: > "))
        return guessedNumber

def number_compare():
    target = generate_number()
    for i in range(0,3):
        print("Attempt", i+1)
        time.sleep(2)
        guess = user_guesser()
        time.sleep(2)
        if guess== target:
            print("That's correct, you win!")
            break
        else:
            print("That is not the correct number")
            time.sleep(2)



number_compare()

