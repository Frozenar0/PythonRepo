#find if a string is empty/blank

def findBlankStr(str):
    str = str.replace(" ", "")
    if len(str) == 0:
        print("this string is blank")
    else:
        print ("this string is not blank")



findBlankStr("")
findBlankStr(" ")
findBlankStr("hello")