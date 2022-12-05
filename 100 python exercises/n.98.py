#check wheter a number is symmetrical or not

def symmetryCheck(num):

    if str(num) == (str(num)[::-1]):



        print(num, "is symmetric!")
    else:
        print(num, "is not symmetric!")

symmetryCheck(243)