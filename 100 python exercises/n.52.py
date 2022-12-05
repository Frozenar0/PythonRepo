# display a rhombus

def pyramid(base):
    layers = 1
    layer = []
    while layers < base+1:
        for i in range(layers):
            layer.append(" * ")
        for i in range(base-(len(layer))):
            layer.insert(0, " ")

        layers += 1
        print(" ".join(layer))
        layer = []


def inverted_pyramid(base):
    layers = base
    layer = []
    while layers+1 > 0:
        for i in range(layers):
            layer.append(" * ")
        for i in range(base+1-(len(layer))):
            layer.insert(0, " ")
        layers -= 1
        print(" ".join(layer))
        layer = []


def make_rhombus(base):
    pyramid(base)
    inverted_pyramid(base-1)


make_rhombus(10)
