#write a pattern that prints the following pattern@
#A
#BB
#CCC
#DDDD
#EEEEE


def fuckThisLetter(base):
    layers = 0
    layer = []
    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    #builds a layer
    while layers < base:
        for i in range(layers+1):
            layer.append(alph[layers])

    #pushes layer, sets counter and resets variable
        layers +=1
        print(" ".join(layer))
        layer=[]

fuckThisLetter(5)