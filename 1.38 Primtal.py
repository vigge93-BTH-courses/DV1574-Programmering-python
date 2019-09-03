import math


def is_prime(number):
    """
    Returns True if number is prime, otherwise returns False.

    Keyword arguments:
    number -- Number to test
    """
    if type(number) != int or number <= 1:
        return False
    res = True
    for i in range(2, math.ceil(math.sqrt(number) + 1)):
        if number % i == 0 and i != number:
            res = False
            break
    return res


print(is_prime(97))
print(is_prime(1))
print(is_prime(-2))
print(is_prime(10))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(6.5))
print(is_prime('Apa'))
