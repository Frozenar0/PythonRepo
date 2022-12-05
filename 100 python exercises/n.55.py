#write a program to delete an element from a given index


def deleteElem(list, delete):
    del list[delete]
    print(list)

deleteElem(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], 1)