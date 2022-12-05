#write a program to replace specific given character in string

def charRepl(string, charOut, charIn):
    stringList= [*string]
    for i in range(len(stringList)):
        if stringList[i] == charOut:
            stringList[i] = charIn
        else:
            continue


    print(stringList)

charRepl("hello World","o","0")