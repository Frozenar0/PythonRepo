#write a program to find the product of all prime numbers in a list

import numpy as np
def whatTheActualFUck(list):
    odds =[]
    for i in list:
        if checkIfPrime(i) is True:
            odds.append(i)
    print(np.prod(odds))


def checkIfPrime(num):
    if num > 1:
        for i in range (2, int(num/2)+1):
            if (num % i) == 0:
                return True
                break
            else:
                return False
    else:
        return False

whatTheActualFUck([2,3,5,66,88,99])