import time
import random

def compare_nums(guessList, userNumber):
     for i in guessList:
         time.sleep(2)
         print("computer has guessed ", i)
         time.sleep(2)
         if i == userNumber:
             print("Computer has guessed right!")
             print("Computer wins!")
             break
         else:
             print("Computer has guessed wrong!")

# compare_nums([3,1,2], 3)


userNumber = input("please insert a number between 1 and 10 > ")
guessList = random.sample(range(1,4), 3)
for i in guessList:
    time.sleep(2)
    print("computer has guessed ", i)
    time.sleep(2)
    print(i)
    print(userNumber)
    if i == userNumber:
        print("Computer has guessed right!")
        print("Computer wins!")
        break
    else:
        print("Computer has guessed wrong!")