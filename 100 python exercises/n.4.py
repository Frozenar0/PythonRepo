#write a prigram which swaps two variables

def swappino(num1, num2):
    print("a=",num1)
    print("b=", num2)
    print("swapped a=", num2)
    print("swapped b=", num1)

#this is a dumb exercise that could've been worded better, This is probably the solution that it was trying to elicit
def swapperino(num1, num2):
    a = num1
    b = num2
    print("a=", a)
    print("b=", b)
    a, b = b, a
    print("a=", a)
    print("b=", b)

swappino(10,20)
swapperino(5,30)