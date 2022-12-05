#write a program to find the product of all even numbers in a list

import numpy as np
def whatTheActualFUck(list):
    odds =[]
    for i in list:
        if i % 2 == 0:
            odds.append(i)
    print(np.prod(odds))

whatTheActualFUck([1,3,2,4,3,5])