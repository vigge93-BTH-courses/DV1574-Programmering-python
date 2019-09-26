import math


def pythagoras(a, b, C=math.pi/2):
    """
    Calculates length of the third side of triangle using cosine formula.

    Keyword arguments:
    a -- Side a of the triangle
    b -- Side b of the triangle
    C -- Angle opposite side c of triangle (default PI/2)
    """
    return math.sqrt(a ** 2 + b ** 2 - 2*a*b*math.cos(C))


print(pythagoras(3, 4))
print(pythagoras(4, 5, 1))
