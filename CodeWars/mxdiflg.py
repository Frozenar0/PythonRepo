def mxdiflg(a1, a2):
    result = 0
    print(not a1, not a2)
    if not a1 or not a2:
        result = -1
    elif a1 is None or a2 is None:
        result = -1
    else:
        for x in a1:
            for y in a2:
                if (len(x) - len(y)) > result:
                    result = len(x) - len(y)
        for x in a2:
            for y in a1:
                if (len(x) - len(y)) > result:
                    result = len(x) - len(y)

    return result



s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))

s1 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
s2 = ["bbbaaayddqbbrrrv"]
print(mxdiflg(s1, s2))

s2 = []
s1 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2))







