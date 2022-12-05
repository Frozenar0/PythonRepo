#write a program to create a matrix filled with ones

import numpy as np

def matrixGen1(row, column):
    val = [0] * row
    for x in range (row):
        val[x] = [1] * column
    print(np.array(val))


matrixGen1(3,4)