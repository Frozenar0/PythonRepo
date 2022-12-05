#write a program to check wether a given string is upper case or lower case

def caseChecker(string):
    if string.isupper() == True:
        print(string, "is upper case")
    else:
        print(string, "is lower case")

caseChecker("HELLO")
caseChecker("hello")
caseChecker("heLLO")
caseChecker("HELlo")
