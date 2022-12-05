#write a program to check for leap year

def checkLeap(year):
    if((year % 400 == 0) or
        (year % 100 != 0) and
        (year % 4 == 0)):
        print("this year is a leap year")
    else:
        print("this is not a leap year")

checkLeap(2022)
checkLeap(2023)
checkLeap(2024)
checkLeap(2025)
        