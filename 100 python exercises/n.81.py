#create a matrix filled with zeros

import numpy as np

def matrixGen0(row, column):
    val = [0] * row
    for x in range (row):
        val[x] = [0] * column
    print(np.array(val))


matrixGen0(3,4)