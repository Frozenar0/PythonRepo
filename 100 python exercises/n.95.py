#write a program to count vowels and consonants in a string

def VoCoCounter(string):
    vowels = ["a","e","i","o","u"]
    voCount = 0
    coCount = 0
    splitString = [*string]
    for letter in splitString:
        if letter.lower() in vowels:
            voCount +=1
        else:
            coCount +=1

    print(string)
    print("Vowels = ", voCount)
    print("consonants = ", coCount)

VoCoCounter("apple")