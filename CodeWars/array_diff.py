def array_diff(a, b):
    answer =[]
    for i in range(len(a)):
        if a[i] not in b:
            answer.append(a[i])
    return answer


print(array_diff([1,2,2], [2]))


