long = []
short =[]

def remove_common(long, short):
    for i in long[:]:
        if i in short:
            long.remove(i)
            short.remove(i)

    print("list1 : ", long)
    print("list2 : ", short)


remove_common(long, short)