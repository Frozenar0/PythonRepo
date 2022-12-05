def digitize(n):
    n = [int(x) for x in str(n)]
    n.reverse()
    return(n)

print(digitize(123456))