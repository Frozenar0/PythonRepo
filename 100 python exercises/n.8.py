#find a program to find the largest number in a list/array
def findMax(*args):
    max = 0
    for i in args:
        if i > max:
            max = i
        else:
            continue
    print (max)


findMax(1,2,3,4,2,5,6,33,5,3,230,5,22)


