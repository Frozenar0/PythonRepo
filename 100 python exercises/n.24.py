#write a program that sorts words in alfphabetical order

def wordSorter(str):
    #divide the words into an array where each element of it is a word
    sortedStr = [word.lower() for word in str.split()]

    #array.sort, then print it
    sortedStr.sort()
    for word in sortedStr:
        yield word


for word in wordSorter("hello my name is Alessandro Inguscio and I am trying to sort this sentence"):
    print(word)