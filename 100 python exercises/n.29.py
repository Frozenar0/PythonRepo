#write a program that generates a prime number series


def primeSeries(end):
    for n in range(2, end):
        for x in range(2, n):
            if n % x == 0:
                break
            else:
                yield n


print(*set(primeSeries(100)))