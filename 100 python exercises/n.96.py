#write a program to remove every vowel from a string


def VowelEraser(string):
    vowels = ["a","e","i","o","u"]
    splitString = [*string]
    resultString = []
    for letter in splitString:
        if letter.lower() not in vowels:
            resultString.append(letter)
        else:
            continue

    print(resultString)
    print(''.join(resultString))


VowelEraser("I am not happy")
