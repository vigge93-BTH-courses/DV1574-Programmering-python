import math


def pi():
    """
    Calculate pi using Ramanujans algorithm to a precision of 10^-15.
    """
    sum = 0
    val = 1
    k = 0
    while val > 10**(-15):
        val = (math.factorial(4 * k) * (1103 + 25390 * k)) / \
            (math.factorial(k) ** 4 * 396 ** (4 * k))
        sum += val
        k += 1
    return 9801/(sum * 2 * math.sqrt(2))


print(pi())
