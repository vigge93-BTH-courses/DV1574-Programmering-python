def unit(n):
    return n % 10


def ten(n):
    return (n // 10) % 10


def digit(num, n):
    return (num // 10 ** (n-1)) % 10


print(unit(123))
print(ten(123))
print(digit(1234, 2))
print(digit(1234, 4))
