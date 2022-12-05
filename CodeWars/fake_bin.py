def fake_bin(x):
    numlist= [*x]
    result = []
    for i in numlist:
        print(numlist)
        if int(i) > 4 :
            result.append("1")
        else:
            result.append("0")
    return "".join(result)

fake_bin("1234567890")