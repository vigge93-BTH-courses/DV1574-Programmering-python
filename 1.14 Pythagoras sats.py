import math


def pythagoras(a, b, C=math.pi/2):
    return math.sqrt(a ** 2 + b ** 2 - 2*a*b*math.cos(C))


print(pythagoras(3, 4))
print(pythagoras(4, 5, 1))
