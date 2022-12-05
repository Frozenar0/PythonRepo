#write a progrma that performs addition, subtraction, multiplication and division on two given matrices
X = [[2,7,3],
     [4,5,6],
     [7,8,9]]

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]


resultSum = [[X[i][j] + Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

resultSub = [[X[i][j] - Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

resultMult = [[X[i][j] * Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

resultDiv = [[X[i][j] / Y[i][j] for j in range
(len(X[0]))] for i in range(len(X))]

print("sum:")
for r in resultSum:
    print(r)

print("subtraction:")
for r in resultSub:
    print(r)

print("Multiplication:")
for r in resultMult:
    print(r)
    
print("Division:")
for r in resultDiv:
    print(r)

