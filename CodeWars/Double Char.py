def double_char(string):
    newString = []
    for character in string:
        newString.append(character)
        newString.append(character)
    print(''.join(newString))

double_char("baNAnarama")