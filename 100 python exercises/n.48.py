#write a program that displays an inverted pyramid


def InvertedPyramid(base):
    layers = base
    layer = []
    while layers+1 > 0:
        for i in range(layers):
           layer.append(" * ")
        for i in range(base-(len(layer))):
            layer.insert(0, " ")
        layers -=1
        print(" ".join(layer))
        layer = [ ]

InvertedPyramid(5)