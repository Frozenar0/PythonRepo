#write a program to reverse a given string

def reverseStr(str):
    revStr=[]
    for i in range(len(list(str))):
        revStr.insert(0, str[i])
    print(" ".join(revStr))

reverseStr("hello world, 123")