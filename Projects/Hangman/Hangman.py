# one player thinks of a word
# he draws as many blank spaces as there are letters in the chosen word
# player two starts guessing letters
# if the guessed letter is in the chosen word, one of the blanks is filled
# player two has 11 attempts to guess the word that player one is thinking of
# if all the attempts are used the man is hanged and player one wins
# if the word is guessed player two wins
#
#I need a dictionary to compare chosen_word and guessed_word,because I will need to compare the exact positions of the letters


# MENU


import time as tm
import random as rm

player_number = 0
difficulty = 0
guessed_word = ""
chosen_word = ""

#lits of words to be used when playing against computer. pc will chose randomly from a list (list chosen by difficulty)
hard_words = ["Jazz","Kiwifruit","Horror","Quiz","Rhythm","Cowboy","Zombie","Bookworm","Nymph","Jacuzzi","Zodiac", "Whiskey"]
easy_words = ["Pool","Mama","Egg","Fire","Arm","Sun","Dinner","Free","Horse","Book","Ice","Sea","Home","Cross","Funny","House","Bed","Door","Hair","Good","Rain","Drink","Eye","Blood","Dog"]

def menu():
    while True:
        #global difficulty
        #global player_number
        print("HANGMAN")
        tm.sleep(1)
        print("Select number of players")
        tm.sleep(1)
        print("type 1 for player vs computer")
        tm.sleep(1)
        print("type 2 for player vs player")
        tm.sleep(1)
        player_number = int(input(">>> "))
        tm.sleep(2)
        if player_number == 1:
            print("Select difficulty")
            tm.sleep(1)
            print("type 1 for hard")
            tm.sleep(1)
            print("type 2 for easy")
            tm.sleep(1)
            print("type 2 for easy")
            tm.sleep(1)
            difficulty = input(">>> ")
            break
        else:
            break
    return player_number, difficulty





def one_player_hangman():
    #this will be the one player vs computer loop
    pass

def two_player_hangman():
    #this will be the player vs player loop
    pass

def word_chooser(difficulty):
    #chooses the word from the word lists to be used in one player hangman
    if difficulty == 1:
        return (rm.choice(hard_words))
    else:
        return (rm.choice(easy_words))
    

def word_comparer():
    # function to compare words chosen words with guessed words and return the number of correct letters guessed
    #should this be where I put the dictionary generator as well? no, see dictionary_generator()

    pass

def hangman_drawer():
    #draws as many blank spaces as there are letters in the the chosen_word, fills in the blanks when a letter has been guessed correctly, shows how many attempts are left
    pass

def dictionary_generator(chosen_word):
    #grabs the chosen words and creates a dictionary where keys are the letters of chosen word and values are empty (to be filled with guessed_letters)
    word_dictionary = {}
    chosen_letters = [i for a,i in enumerate(chosen_word)] 
    for letter in chosen_letters:
        word_dictionary[letter] = ''
    return word_dictionary




def main_loop():
    while True:
        menu()
        if player_number == 1:
            one_player_hangman()
        else:
            two_player_hangman()



print(dictionary_generator(word_chooser(1)))