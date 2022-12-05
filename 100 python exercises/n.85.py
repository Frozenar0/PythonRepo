#write a program to check whether a number is devisible by 5 or not


def check5(num):
    if num % 5 == 0:
        print(num, "is divisible by 5")
    else:
        print(num, "is not divisible by 5")


check5(-5)
check5(0)
check5(1)
check5(15)
check5(1239826347861812460)