# step 1 take user value
# generate computer value
# compare
# print result
#
# TO DO
# make a menu so you can decide how many times you want to play, keep play until you say stop
# input validation


import time
import random
selection = ["rock", "paper", "scissor"]


def userValueGenerator():
    while True:
        userValue = (input("rock, paper or scissor? ")).lower()
        if userValue in selection:
            return userValue
        else:
            print("please select rock, paper or scissor")


def computerValueGenerator():
    time.sleep(2)
    choice = random.choice(selection)
    print ("Computer chose", choice)
    time.sleep(2)
    return choice


def comparator(userValue, computerValue):

    lossMessage = "You lose!"
    winMessage = "You win!"

    if userValue == computerValue:
        #draw
        print("it's a draw!")
    elif userValue == "rock":
        if computerValue == "scissor":
            #win
            print(winMessage)
        else:
            #loss
            print(lossMessage)
    elif userValue == "paper":
        if computerValue == "rock":
            #win
            print(winMessage)
        else:
            #loss
            print(lossMessage)
    elif userValue == "scissor":
        if computerValue == "paper":
            #win
            print(winMessage)
        else:
            #loss
            print(lossMessage)


comparator(userValueGenerator(), computerValueGenerator())
    