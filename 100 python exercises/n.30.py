#write a program to generate a fibonacci series

def fibo(range):
    n1 = 0
    n2 = 1
    count=0
    while count < range:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count += 1

print(fibo(100))