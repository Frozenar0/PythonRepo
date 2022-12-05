#find the most frequent number from a list/array

def findBig(list):
    counter = 0
    num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        print("list.count= ", list.count(i))
        print("counter= ", counter)
        if(curr_frequency>counter):
            counter = curr_frequency
            num = i

    return num

list = [2,7,3,2,1,2,1,3,1,1]
print(findBig(list))