#write a program that displays a pyramid


def pyramid(base):
    layers = 1
    layer = []
    while layers < base+1:
        for i in range(layers):
           layer.append(" * ")
        for i in range(base-(len(layer))):
            layer.insert(0, " ")

        layers +=1
        print(" ".join(layer))
        layer = [ ]

pyramid(10)
