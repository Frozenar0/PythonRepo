#find interesction of two lists

def vennDia(list1, list2):
    print([value for value in list1 if value in list2])

vennDia([1,2,3,4,5],[3,4,5,6,7])