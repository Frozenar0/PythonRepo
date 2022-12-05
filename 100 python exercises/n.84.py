#write a function that takes a list and returns the maximum number

def maxNum(list):
#   print(max(list))
    result=0
    for i in list:
        if i > result:
            result = i
        else:
            continue
    print(result)



maxNum([2,3,4,55,66,77,88,33])


