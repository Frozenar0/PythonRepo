#write a program to separate numbers and english alphabet chafacters from a string

def numAndLets(string):
    numList =[]
    alphaList = []
    stringList = [*string]
    for i in stringList:
        if i.isalpha():
            alphaList.append(i)
        else:
            numList.append(i)
    print(''.join(numList))
    print(''.join(alphaList))

numAndLets("hello 123 i am 444")