#write a program to count capital letters in a given string

def countUpper(string):
    letList = [*string]
    counter = 0
    for i in letList:
        if i.isupper():
            counter +=1
    print(counter)

countUpper("Hello My Name Is Python")