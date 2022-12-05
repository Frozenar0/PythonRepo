#write a program to remove every consonant from a string

def ConsonantEraser(string):
    vowels = ["a","e","i","o","u", " "]
    splitString = [*string]
    resultString = []
    for letter in splitString:
        if letter.lower() in vowels:
            resultString.append(letter)
        else:
            continue

    print(resultString)
    print(''.join(resultString))


ConsonantEraser("Why you are worry")