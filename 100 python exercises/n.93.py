#write a program to check lean year

def checkLeapYear(year):

        if year % 4 == 0 & year % 400 ==0:
            print("leap year")
        else:
            print("not leap year")

checkLeapYear(2000)
checkLeapYear(1904)
checkLeapYear(2002)
checkLeapYear(2003)
checkLeapYear(2004)