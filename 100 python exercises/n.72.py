#remove the first and last character of a string

def charRem(string):
    letList = [*string]
    letList.pop(0)
    letList.pop(len(letList)-1)
    print (''.join(letList))
charRem("I am Happy")