#find unique numbers in a list:


def findUnique(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)

    print(newlist)

findUnique([1,1,2,2,3,4,3,4,5,3,2,5,7,7,5,44,66,3,33,33,4,5,66,66])
