#write a pattern that prints the following pattern@
#1
#12
#123
#1234
#12345


def fuckThis(base):
    layers = 0
    layer = []
    while layers < base:
        for i in range(layers+1):
            layer.append(str(i+1))
        layers +=1
        print(" ".join(layer))
        layer=[]

fuckThis(5)