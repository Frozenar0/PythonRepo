#write a program that displays a rectangle


def makeRectangle(base, height):
    layers=0
    layer=[]
    while layers < height:
        for i in range(base):
            layer.append("*")
        layers +=1
        print(" ".join(layer))
        layer=[ ]


makeRectangle(7,14)

