#find the area of a triangle



# #given three sides, find out if triangle is a rectangle-triangle
# sqa = pow(a, 2)
# sqb = pow(b, 2)
# sqc = pow(c, 2)
#
# if (sqa == sqa + sqb or
#         sqb == sqa + sqc or
#         sqc == sqa + sqb):
#     print("Right-angled Triangle")
#
# #if yes use pythagora
# #a**2+b**2=c**2


#if not use Heron's formula
#we can just use Heron's for all triangles apparently


import math

def triangle_area(a,b,c):
    s = (a+b+c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area


print(triangle_area(5,3,7))