#write a program to replace a specific word in a string

def wordRepl(string, wordOut, wordIn):
    stringList= string.split()
    for i in range(len(stringList)):
        if stringList[i] == wordOut:
            stringList[i] = wordIn
        else:
            continue


    print(stringList)

wordRepl("I am learning python and I am a python developer","python","java")