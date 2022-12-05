#create a function that creates a list from a given range

def listMaker(minNum, maxNum):
    result = []
    for i in range(minNum, maxNum+1):
        result.append(i)
    print(result)
listMaker(3,10)

