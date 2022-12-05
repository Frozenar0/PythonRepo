#write a program to check wheter a number is prime or not
# Program to check if a number is prime or not

num = 86263

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

    # Program to check if a number is prime or not

    num = 407

    # To take input from the user
    # num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num, "is not a prime number")




def findPrime(num1):
    if num1 > 1:
        for i in range (2, num1):
            if (num1 % i) == 0:
                print("not prime because we just devided it by something")
                break
        else:
            print("it prime")




