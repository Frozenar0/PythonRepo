#write a program that displays a rectangle triangle


def pyramid(base):
    layers = 1
    layer = []
    while layers < base+1:
        for i in range(layers):
           layer.append(" * ")
        layers +=1
        print(" ".join(layer))
        layer = [ ]

pyramid(10)