#write a program to find the sum of natural numbers

def natNum(n):
    sum=0
    for i in range(n+1):
        print(i)
        sum= sum+i
        print(sum)
    return sum

print(natNum(16))