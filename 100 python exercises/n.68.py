#find second largest number in a list

def find2ndBiggest(list):
    list.sort()
    checker = list[0]
    for i in range((len(list))):
        if list[i] == checker:
            continue
        else:
            print (list[i])
            break

find2ndBiggest([2,1,1,1,2,2,2,3,44,5,4,77,5])