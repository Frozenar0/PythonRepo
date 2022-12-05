#find how many prime numbers there are in a list


def primeFinder(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return 0
                break
        else:
            return 1
    else:
        return 0

def iterator(list):
    counter = 0
    for i in list:
        counter += primeFinder(i)
    print(counter)

iterator([3,6,7,8,88,9,57])