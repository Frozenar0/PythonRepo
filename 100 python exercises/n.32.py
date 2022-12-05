#write a prigram to remove all duplicates from a given list

def removeDuplicate(list):
    return [*set(list)]


print(removeDuplicate([1,1,2,2,3,3,3,3,4,5,6,5,6,7,4]))