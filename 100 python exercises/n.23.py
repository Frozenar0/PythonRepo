#find a program to find the HCF of two numbers

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


