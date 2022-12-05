# OBJECTIVES:
# Make a game where the computer needs to guess a number input by the user
# step uno: ask user a number and save it
# make a for loop with a set number of iteration (how many tries the computer gets to guess)
# at each iteration the computer generates a random number and compares it to the input
# if number wrong move to next guess, if right, print success statement

import random
import time


def grab_number():
     global userNumber
     userNumber = input("please insert a number between 1 and 10 > ")
     return userNumber
    


def guess_work():
     global guessList
     guessList = random.sample(range(1,10), 3)
     return guessList
    

def compare_nums():
    
    for i in guessList:
        time.sleep(2)
        print("Computer has guessed ", i)
        time.sleep(2)
        if i == int(userNumber):
            print("Computer has guessed right!")
            print("Computer wins!")
            break
        else:
            print("Computer has guessed wrong!")
    
def main():
    grab_number()
    guess_work()
    compare_nums()

main()





