#write a program that finds the factorial of a given number
def factorioEasy(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

def factorioRecursive(n):
    if(n==0):
        return 1
    return n * factorioRecursive(n-1)

print(factorioRecursive(5))