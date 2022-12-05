#write a program to create a matrix filled with a specific value

import numpy as np

def matrixGen(row, column,value):
    val = [0] * row
    for x in range (row):
        val[x] = [value] * column
    print(np.array(val))


matrixGen(3,4,9)