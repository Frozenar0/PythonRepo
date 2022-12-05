#write a program that generates an even number series

import random
def RandNat(n):
    list = []
    for i in range(n):
        list.append(random.randint(0, n))
    list2 = [*set(list)]
    for num in list2:
            if num % 2 == 0:
                print(num)



RandNat(100)